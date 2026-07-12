import streamlit as st
from llm import classify_request
from agents.complaint_agent import process_complaint
from agents.service_agent import process_service
from agents.enquiry_agent import process_enquiry
from database import init_db, save_request
from helpers import display_workflow
import json

st.set_page_config(page_title="Agentic Request Processor", layout="wide")
init_db()

st.title("🤖 Agentic AI Request Processor")
# Load sample requests
with open("sample_requests.json", "r") as f:
    sample_requests = json.load(f)

sample_titles = [""] + [item["title"] for item in sample_requests]

selected_sample = st.selectbox(
    "Choose a Sample Request (Optional)",
    sample_titles
)

st.markdown("""Paste or type a user request below and click **Process Request** to classify and route it.""")

request = ""

if selected_sample:
    request = next(
        item["request"]
        for item in sample_requests
        if item["title"] == selected_sample
    )

request = st.text_area(
    "Paste customer request",
    value=request,
    height=200
)

if st.button("Process Request"):

    if not request.strip():
        st.warning("Please enter a request.")
        st.stop()

    with st.spinner("AI is analysing..."):
        result = classify_request(request)

    label = result["label"].lower()

    st.success("Classification Complete")

    st.subheader("AI Classification")
    st.json(result)

    # ----------------------
    # Route to correct agent
    # ----------------------

    if "complaint" in label:

        workflow = process_complaint(request, result)
        save_request(
            request,
            result["label"],
            result["urgency"],
            result["confidence"],
            workflow["assigned_team"],
            workflow["status"]
        )
        display_workflow("Complaint Workflow", workflow)

    elif "service" in label:

        workflow = process_service(request, result)
        save_request(
            request,
            result["label"],
            result["urgency"],
            result["confidence"],
            workflow["assigned_team"],
            workflow["status"]
        )
        display_workflow("Service Request Workflow", workflow)

    elif "enquiry" in label:

        workflow = process_enquiry(request, result)
        save_request(
            request,
            result["label"],
            result["urgency"],
            result["confidence"],
            workflow["assigned_team"],
            workflow["status"]
        )

        display_workflow("General Enquiry Workflow", workflow)