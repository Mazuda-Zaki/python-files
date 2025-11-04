import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="BMI Calculator", layout="centered", page_icon="⚖️")

st.title("🧮 BMI Calculator")
st.write("Let's Calculate Your **Body Mass Index (BMI)** And Understand What It Means.")

st.header("🧑🏻‍💻 Enter Your Details Below:")

# Get user input
weight = st.number_input("Enter your weight (in kg)", min_value=10, max_value=200, value=65)
height = st.number_input("Enter your height (in cm)", min_value=50, max_value=250, value=170)

st.write("🏋️ Your weight is:", weight, "kg")
st.write("🪜 Your height is:", height, "cm")

# Calculate BMI when user clicks the button
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        height_m = height / 100  # Convert cm to m
        bmi = weight / (height_m ** 2)

        # Display BMI and category
        st.success(f"Your BMI is: **{bmi:.2f}**")

        # BMI Categories
        if bmi < 18.5:
            category = "Underweight 😤"
            color = "#96D6E3"
        elif 18.5 <= bmi < 25:
            category = "Normal 😏"
            color = "#87F1AA"
        elif 25 <= bmi < 30:
            category = "Overweight 🧐"
            color = "#DFC714BA"
        else:
            category = "Obese 🤔"
            color = "#F00A0AB9"

        st.markdown(
            f"""
            <div style="padding: 15px; border-radius: 10px; background-color: {color}; text-align: center;">
                <h3>Your BMI Category: {category}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

# Chart (outside button block)
st.header("📊 BMI Range Chart")
 
# Data
bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal", "Overweight", "Obese"],
    "Range": [18.5, 24.9, 29.9, 40]
})
 
# Define custom colors for each category
color_scale = alt.Scale(
    domain=["Underweight", "Normal", "Overweight", "Obese"],
    range=["#96D6E3", "#87F1AA", "#DFC714BA", "#F00A0AB9"]
)
 
# Create chart
chart = (
    alt.Chart(bmi_data)
    .mark_bar()
    .encode(
        x=alt.X("Category:N", title="BMI Category"),
        y=alt.Y("Range:Q", title="BMI Range"),
        color=alt.Color("Category:N", scale=color_scale, legend=None)
    )
    .properties(width=600, height=400)
)
 
st.altair_chart(chart, use_container_width=True)