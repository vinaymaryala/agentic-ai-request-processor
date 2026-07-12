def process_service(request: str, classification: dict):
    """
    Process a service request and generate a remediation workflow.
    """

    category = classification.get("category", "General").lower()
    urgency = classification.get("urgency", "Medium").title()

    # ----------------------------
    # Determine responsible team
    # ----------------------------

    if category == "profile update":
        assigned_team = "Customer Operations"

    elif category == "maintenance":
        assigned_team = "Technical Operations"

    elif category == "payment":
        assigned_team = "Financial Operations"

    elif category == "account":
        assigned_team = "Account Management"

    else:
        assigned_team = "Operations"

    # ----------------------------
    # Follow-up SLA
    # ----------------------------

    follow_up_map = {
        "High": "4 Hours",
        "Medium": "24 Hours",
        "Low": "3 Days"
    }

    follow_up = follow_up_map.get(urgency, "24 Hours")

    # ----------------------------
    # Workflow Actions
    # ----------------------------

    actions = [
        "Service request received",
        "Customer information verified",
        f"Assigned to {assigned_team}",
        "Service request logged",
        "SLA timer started",
        f"Follow-up scheduled ({follow_up})"
    ]

    if category == "profile update":
        actions.extend([
            "Validate customer identity",
            "Update requested profile information",
            "Notify customer of successful update"
        ])

    elif category == "maintenance":
        actions.extend([
            "Create maintenance work order",
            "Assign field engineer",
            "Schedule maintenance visit"
        ])

    elif category == "payment":
        actions.extend([
            "Validate payment request",
            "Forward to finance team",
            "Confirm completion with customer"
        ])

    elif category == "account":
        actions.extend([
            "Review account information",
            "Apply requested account changes",
            "Notify customer"
        ])

    else:
        actions.append("Process service request")

    # ----------------------------
    # Draft Response
    # ----------------------------

    draft_response = f"""
Dear Customer,

Thank you for your service request.

Your request has been assigned to our {assigned_team}.

Priority: {urgency}

Expected Completion: {follow_up}

We will notify you once the request has been completed.

Regards,

Customer Support Team
"""

    return {
        "assigned_team": assigned_team,
        "priority": urgency,
        "status": "In Progress",
        "follow_up": follow_up,
        "actions": actions,
        "draft_response": draft_response
    }