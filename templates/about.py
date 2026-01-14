import streamlit as st

# Profile Name Session
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/Logo-design-template-on-transparent-background-PNG.png", width=250)

with col2:
    st.title("General Kenobi", anchor=False)
    st.write("Data Analyst Pro")


# Qualifications
st.write("\n")
st.subheader("Qualifications", anchor=False)
st.write(
    """
    - X years of Experience doing blah
    """
)


# Skills Session
st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - X years of Experience doing blah
    """
)