import streamlit as st
import pandas as pd

from database import get_requests

st.set_page_config(page_title="Dashboard")

st.title("📊 Processing Dashboard")

def color_status(status):

    if status == "Open":
        return "🟠 Open"

    if status == "Resolved":
        return "🟢 Resolved"

    if status == "In Progress":
        return "🔵 In Progress"

    return status 

rows = get_requests()

if not rows:
    st.info("No requests processed yet.")
    st.stop()
    

df = pd.DataFrame(
    rows,
    columns=[
        "ID",
        "Request",
        "Category",
        "Urgency",
        "Confidence",
        "Assigned Team",
        "Status",
        "Created At"
    ]
)
df["Status"] = df["Status"].apply(color_status)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Requests", len(df))

col2.metric(
    "Complaints",
    len(df[df["Category"] == "Complaint"])
)

col3.metric(
    "Service Requests",
    len(df[df["Category"] == "Service Request"])
)

col4.metric(
    "General Enquiries",
    len(df[df["Category"] == "General Enquiry"])
)

st.subheader("Request History")

st.dataframe(
    df[
        [
            "Category",
            "Urgency",
            "Confidence",
            "Assigned Team",
            "Status",
            "Created At"
        ]
    ],
    width="stretch"
)

st.subheader("Requests by Category")

st.bar_chart(df["Category"].value_counts())

st.subheader("Urgency Distribution")

st.bar_chart(df["Urgency"].value_counts())