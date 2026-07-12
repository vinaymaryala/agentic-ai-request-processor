import streamlit as st


def display_workflow(title, workflow):
    """
    Display a workflow summary with team info, priority, status, actions, and draft response.
    
    Args:
        title (str): The title/subheader for the workflow section
        workflow (dict): Dictionary containing workflow details with keys:
            - assigned_team: Team name
            - priority: Priority level
            - status: Current status
            - follow_up: Follow-up information
            - actions: List of action items
            - draft_response: Draft response text
    """
    st.subheader(title)

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Assigned Team: {workflow['assigned_team']}")
        st.write(f"Priority: {workflow['priority']}")
        st.success(f"Status: {workflow['status']}")

    with col2:
        st.write(f"Follow Up: {workflow['follow_up']}")

    st.write("### Actions")

    for action in workflow["actions"]:
        st.write(f"✅ {action}")

    st.text_area(
        "Draft Response",
        workflow["draft_response"],
        height=220,
        label_visibility="collapsed",
    )
