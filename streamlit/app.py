import streamlit as st
import requests

st.title("🎓 Student Performance Prediction")

# --- Collect inputs from user ---
age = st.number_input("Age", min_value=1, max_value=120)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
p_class = st.text_input("Class (e.g., 10th)")
study_hours = st.number_input("Study Hours per Day", min_value=0.0, max_value=24.0)
attendance = st.slider("Attendance (%)", 0, 100, 90)
math_score = st.slider("Math Score (%)", 0, 100, 85)
science_score = st.slider("Science Score (%)", 0, 100, 80)
english_score = st.slider("English Score (%)", 0, 100, 75)
passed = st.checkbox("Passed")

if st.button("Predict"):
    data = {
        "age": age,
        "gender": gender,
        "p_class": p_class,
        "study_hours": study_hours,
        "attendance": attendance,
        "math_score": math_score,
        "science_score": science_score,
        "english_score": english_score,
        "passed": passed
    }

    res = requests.post("http://127.0.0.1:8000/predict", json=data)
    
    if res.status_code == 200:
        result = res.json()
        st.success(f"🎯 Prediction: {result['prediction']}")
        st.json(result["input_data"])
    else:
        st.error(f"❌ Error: {res.text}")
