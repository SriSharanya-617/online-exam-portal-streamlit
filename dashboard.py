import streamlit as st
from supabase_client import supabase

def dashboard_page():
    user = st.session_state['user']
    st.title(f"📊 Dashboard - {user['name']} ({user['role']})")

    if user['role'] == 'admin':
        st.subheader("Admin Panel: Add Questions")
        question = st.text_input("Question")
        option1 = st.text_input("Option 1")
        option2 = st.text_input("Option 2")
        option3 = st.text_input("Option 3")
        option4 = st.text_input("Option 4")
        correct = st.selectbox("Correct Option", [option1, option2, option3, option4])

        if st.button("Add Question"):
            if question and option1 and option2 and option3 and option4 and correct:
                supabase.table("questions").insert({
                    "question": question,
                    "option1": option1,
                    "option2": option2,
                    "option3": option3,
                    "option4": option4,
                    "correct_option": correct
                }).execute()
                st.success("✅ Question added successfully!")

    else:
        st.write("Welcome, student! Click below to start exam.")
        if st.button("Start Exam"):
            st.session_state["page"] = "Exam"

    if st.button("Logout"):
        st.session_state.clear()
        st.session_state["page"] = "Login"
