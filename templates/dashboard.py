import streamlit as st
import pandas as pd

# Configuration Session
YEAR = 2023
P_YEAR = 2022
CITIES = ["Tokyo", "Yokohama", "Osaka"]
DATA = "https://raw.githubusercontent.com/doerayme1224-bot/sales/refs/heads/main/data/sales.csv"

# this section stores things in variables that we will use within our dashboard later, keep in mind that they correspond with attributes in our data

st.title("Dashboard of Sales", anchor=False) # creates a title using streamlit, sets anchor to FALSE as a way to make it show up only on this page

# Caching Data Session
@st.cache_data
def get_and_prepare_data(data): # creates a function that reads a data set, and assigns it new features
    df = pd.read_csv(data).assign(
        date_of_sale=lambda df: pd.to_datetime(df["date_of_sale"]), # creates a date_of_sale feature that converts the date of sale column to a datetime
        month=lambda df: df["date_of_sale"].dt.month, # creates a month feature that gets the month for each sale
        year=lambda df: df["date_of_sale"].dt.year, # creates a year feature that gets the year for each sale
    )
    return df # returns/stores the df

df = get_and_prepare_data(data=DATA) # creates a df using our function and our data which was assigned in configuration sessions

# Calculation of the total revenue and percentage for each city and year Session
city_revenues = (
    df.groupby(["city", "year"])["sales_amount"] # groups our data by the city and the year, to find the sales ammount forr each city and year
    .sum() # adds them to get a total sales amount by  city and year
    .unstack() # converts data from a long format to a short format (pivots the level we made from a from a row to a column)
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] * 100) # creates a new column with assign to calculate the percent change relative to the previous columns value
)
# Displaying Data for each city in separate columns Session
columns = st.columns(3) # sets a stramlit app with three columns
for i, city in enumerate(CITIES): # usees thes columns to find the city revenues for each city
    with columns[i]:
        st.metric( # displays the metrics in the app above the dropdowns, shows there city name, value, and percent change as an arrow
            label=city,
            value=f"$ {city_revenues.loc[city, YEAR]:,.0f}",
            delta=f"{city_revenues.loc[city, 'change']:.0f}% change vs. PY",
        )

# Fields Selection Session
left_col, right_col = st.columns(2)
analysis_type = left_col.selectbox(
    label="Analysis by:", # creates the first select box for the visual on the app, groups it either by the product category or the month and you select it using a dropdown
    options=["Month", "Product Category"],
    key="analysis_type",
)
selected_city = right_col.selectbox("Select a city:", CITIES) # creates the next dropdown, where you select one of the cities from the select a city dropdown 
# Session to Toggle for selecting the year for visualization
previous_year_toggle = st.toggle( # creaets a toggle where you select if you want the current year (unselected) or the previous year within the data
    value=False, label="Previous Year", key="switch_visualization"
)
visualization_year = P_YEAR if previous_year_toggle else YEAR
# Session to Display the year above the chart based on the toggle switch
st.write(f"**Sales for {visualization_year}**") # title thing above the graph

# Filter data based on selection for visualization
if analysis_type == "Product Category": # this filters the data based on the selection that you chose from the dropdown menu
    filtered_data = (
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("product_category", dropna=False)["sales_amount"] # this filters the data based on if you selected product category
        .sum()
        .reset_index()
    )
else: # runs when the first if statement doesn't run
    # Group by month number
    filtered_data = ( # stores the result of the query in a variable filtered_data
        df.query("city == @selected_city & year == @visualization_year")
        .groupby("month", dropna=False)["sales_amount"] # filters based on the year
        .sum()
        .reset_index()
    )
    # Ensure month column is formatted as two digits for consistency
    filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")
# Display the data Session
st.bar_chart(filtered_data.set_index(filtered_data.columns[0])["sales_amount"]) # creates a visual using filtered_data and sets its index/axis to 0 meaning the x axis and shows summary statistics based on the sales amount of the filtered group