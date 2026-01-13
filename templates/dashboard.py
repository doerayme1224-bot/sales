import streamlit as st
import pandas as pd

# Configuration Session
YEAR = 2023
P_YEAR = 2022
CITIES = ["Tokyo", "Yokohama", "Osaka"]
DATA = "https://raw.githubusercontent.com/doerayme1224-bot/sales/refs/heads/main/data/sales.csv?token=GHSAT0AAAAAADTAEANMF646SZUQMR5WO6YC2LG3DLQ"

st.title("Dashboard of Sales", anchor=False)

# Caching Data Session
@st.cache_data
def get_and_prepare_data(data):
    df = pd.read_csv(data).assign(
        date_of_sale=lambda df: pd.to_datetime(df["date_of_sale"]),
        month=lambda df: df["date_of_sale"].dt.month,
        year=lambda df: df["date_of_sale"].dt.year,
    )
    return df

df = get_and_prepare_data(data=DATA)
# Calculation of thetotal revenue and percentage for each city and year Session
city_revenues = (
    df.groupby(["city", "year"])["sales_amount"]
    .sum()
    .unstack()
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] * 100)
)
# Displaying Data for each city in separate columns Session
columns = st.columns(3)
for i, city in enumerate(CITIES):
    with columns[i]:
        st.metric(
            label=city,
            value=f"$ {city_revenues.loc[city, YEAR]:,.0f}",
            delta=f"{city_revenues.loc[city, 'change']:.0f}% change vs. PY",
        )

# Fields Selection Session
left_col, right_col = st.columns(2)
analysis_type = left_col.selectbox(
    label="Analysis by:",
    options=["Month", "Product Category"],
    key="analysis_type",
)
selected_city = right_col.selectbox("Select a city:", CITIES)
# Session to Toggle for selecting the year for visualization
previous_year_toggle = st.toggle(
    value=False, label="Previous Year", key="switch_visualization"
)
visualization_year = P_YEAR if previous_year_toggle else YEAR
# Session to Display the year above the chart based on the toggle switch
st.write(f"**Sales for {visualization_year}**")

# Filter data based on selection for visualization
if analysis_type == "Product Category":
    filtered_data = (
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("product_category", dropna=False)["sales_amount"]
        .sum()
        .reset_index()
    )
else:
    # Group by month number
    filtered_data = (
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("month", dropna=False)["sales_amount"]
        .sum()
        .reset_index()
    )
    # Ensure month column is formatted as two digits for consistency
    filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")
# Display the data Session
st.bar_chart(filtered_data.set_index(filtered_data.columns[0])["sales_amount"])