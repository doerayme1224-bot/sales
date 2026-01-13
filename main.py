import streamlit as st



st.title("Hello World!")

# --- Pages Section Setup ---

about_page = st.Page(
    "templates/about.py",
    title="About me",
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    "templates/dashboard.py", title="Sales Dashboard", icon=":material/bar_chart:"
)

# --- Navigation Session Setup ---
pn = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page],
    }
)


# --- Running Navigation ---
pn.run()





# def main():
#     print("Hello from sales!")


# if __name__ == "__main__":
#     main()