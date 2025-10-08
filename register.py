import streamlit as st
from supabase_client import supabase

def register_page():
    st.title("📝 Register New Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if not (name and email and password):
            st.error("Please fill all fields.")
        else:
            # Insert into the correct table
            response = supabase.table("users").insert({"name": name, "email": email, "password": password}).execute()
            if response.data:
                st.success("✅ Registered successfully! Please log in.")
                st.session_state["page"] = "Login"
            else:
                st.error("Registration failed. Try again.")

    if st.button("Already have an account? Login"):
        st.session_state["page"] = "Login"
