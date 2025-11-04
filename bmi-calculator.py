import streamlit as st
import pandas as pd
import altair as alt

# --- Page Config ---
st.set_page_config(
    page_title="BMI Calculator",
    layout="centered",
    page_icon="⚖️"
)

# --- Custom CSS For Better UI ---
st.markdown("""
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}
.title-box {
    background: #1E88E5;
    padding: 20px;
    border-radius: 12px;
    color: white;
    text-align: center;
}
.input-card, .result-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-top: 15px;
}
.result-category {
    padding: 12px;
    border-radius: 8px;
    font-weight: bold;
    margin-top: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- Title Section ---
st.markdown('<div class="title-box"><h1>⚖️ BMI CALCULATOR</h1><p>Check your body mass index </p></div>', unsafe_allow_html=True)

st.markdown('<div class="input-card">', unsafe_allow_html=True)
st.subheader("🧑‍⚕️ Enter Your Details")

# --- User Inputs ---
weight = st.number_input("Weight (kg)", min_value=10, max_value=200, value=65)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
st.markdown('</div>', unsafe_allow_html=True)


# --- Calculate BMI ---
if st.button("Calculate BMI ✅"):

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Determine Category
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

    # --- Display Result ---
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.success(f"✅ Your BMI: **{bmi:.2f}**")

    st.markdown(
        f"""
        <div class="result-category" style="background:{color}">
            BMI Category: {category}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)


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
