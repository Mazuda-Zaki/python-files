import streamlit as st
import pandas as pd
import altair as alt

# --- Page Config ---
st.set_page_config(
    page_title="BMI Calculator",
    layout="centered",
    page_icon="⚖️"
)

# --- Page Title ---
st.title("⚖️ BMI CALCULATOR")
st.write("Check your Body Mass Index and understand your category.")

# Just add some space before input section
st.write("")  
st.write("")  

st.subheader("🧑‍⚕️ Enter Your Details")

# --- Inputs ---
weight = st.number_input("Weight (kg)", min_value=10, max_value=200, value=65)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)

# --- Calculate BMI ---
if st.button("Calculate BMI ✅"):

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Category logic
    if bmi < 18.5:
        category = "Underweight"
        color = "#96D6E3"
    elif 18.5 <= bmi < 25:
        category = "Normal"
        color = "#87F1AA"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "#DFC714BA"
    else:
        category = "Obese"
        color = "#F00A0AB9"

    st.success(f"✅ Your BMI: **{bmi:.2f}**")

    st.markdown(
        f"""
        <div style="padding: 12px; background:{color}; border-radius:8px; 
        text-align:center; font-weight:bold;">
            BMI Category: {category}
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Chart Section ---
st.subheader("📊 BMI Category Chart")

bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Range": [18.5, 24.9, 29.9, 40]
})

color_scale = alt.Scale(
    domain=["Underweight", "Normal", "Overweight", "Obese"],
    range=["#96D6E3", "#87F1AA", "#DFC714BA", "#F00A0AB9"]
)

chart = (
    alt.Chart(bmi_data)
    .mark_bar()
    .encode(
        x=alt.X("Category:N"),
        y=alt.Y("Range:Q", title="BMI Range"),
        color=alt.Color("Category:N", scale=color_scale, legend=None)
    )
    .properties(width=600, height=350)
)

st.altair_chart(chart, use_container_width=True)
