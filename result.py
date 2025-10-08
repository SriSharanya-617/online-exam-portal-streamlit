import streamlit as st

def result_page():
    st.title("🏆 Result")

    answers = st.session_state.get("answers", {})
    score = 0

    correct_answers = {
        "Q1: 2 + 2 = ?": "4",
        "Q2: Capital of India?": "Delhi"
    }

    for q, correct in correct_answers.items():
        if answers.get(q) == correct:
            score += 1

    st.write(f"Your Score: {score} / {len(correct_answers)}")

    if st.button("Back to Dashboard"):
        st.session_state["page"] = "Dashboard"
