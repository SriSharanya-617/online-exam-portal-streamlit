import streamlit as st
from login import login_page
from register import register_page
from dashboard import dashboard_page
from exam import exam_page
from result import result_page

st.set_page_config(page_title="Online Exam Portal", layout="wide")

# All pages
PAGES = {
    "Login": login_page,
    "Register": register_page,
    "Dashboard": dashboard_page,
    "Exam": exam_page,
    "Result": result_page,
}

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Login"

# Current page
current_page = st.session_state["page"]

# Run the page
if current_page in PAGES:
    PAGES[current_page]()
else:
    st.session_state["page"] = "Login"
    login_page()
