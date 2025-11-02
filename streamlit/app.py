import streamlit as st
import requests

st.set_page_config(page_title="Student Form", page_icon="🎓")
st.title("🎓 Student Data Submission ")

# API endpoint
API_URL = "https://student-api-t2xw.onrender.com/create"

with st.form("student_form"):
    student_id = st.number_input("Roll No", min_value=1, step=1)
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=5, max_value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    p_class = st.text_input("Class", "10th")
    study_hours = st.number_input("Study Hours", min_value=0.0, step=0.5)
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    math_score = st.slider("Math (%)", 0, 100, 80)
    science_score = st.slider("Science (%)", 0, 100, 82)
    english_score = st.slider("English (%)", 0, 100, 78)
    passed = st.checkbox("Passed?", value=True)

    submit = st.form_submit_button("Submit")

if submit:
    data = {
        "student_id": student_id,
        "name": name,
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

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            st.success("✅ Data submitted successfully!")
            st.json(response.json())
        else:
            st.error(f"response_code:({response.status_code})")
            if response.status_code ==400:
                st.error("file already exists ")
            elif response.status_code==201:
                st.success("file successful create")
    except Exception as e:
        st.error(f"🚨 Connection Error: {e}")
