import streamlit as st
from supabase_client import supabase

def login_page():
    st.title("🔐 Online Exam Portal - Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Use the correct table name
        data = supabase.table("users").select("*").eq("email", email).eq("password", password).execute()
        if data.data:
            st.success("Login successful! 🎉")
            st.session_state["user"] = data.data[0]
            st.session_state["page"] = "Dashboard"
        else:
            st.error("Invalid email or password ❌")

    if st.button("New user? Register here"):
        st.session_state["page"] = "Register"
