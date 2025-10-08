import streamlit as st

def exam_page():
    st.title("📝 Exam")

    questions = {
        "Q1: 2 + 2 = ?": ["3", "4", "5", "6"],
        "Q2: Capital of India?": ["Delhi", "Mumbai", "Kolkata", "Chennai"]
    }

    answers = {}

    for q, options in questions.items():
        answers[q] = st.radio(q, options)

    if st.button("Submit Exam"):
        st.session_state["answers"] = answers
        st.session_state["page"] = "Result"
