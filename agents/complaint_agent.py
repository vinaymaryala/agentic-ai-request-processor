def process_complaint(request: str, classification: dict):
    """
    Process a complaint request and generate a remediation workflow.

    Expected classification format:
    {
        "label": "Complaint",
        "category": "Billing",
        "urgency": "High",
        "confidence": <integer between 0 and 100>,
        "reason": "Customer reports duplicate billing."
    }
    """

    category = classification.get("category", "General").lower()
    urgency = classification.get("urgency", "Medium").title()

    # ----------------------------
    # Determine responsible team
    # ----------------------------

    if category == "billing":
        assigned_team = "Billing Support"

    elif category == "technical":
        assigned_team = "Technical Support"

    elif category == "security":
        assigned_team = "Fraud Investigation"

    elif category == "delivery":
        assigned_team = "Logistics"

    elif category == "account":
        assigned_team = "Account Support"

    else:
        assigned_team = "Customer Support"

    # ----------------------------
    # Follow-up SLA
    # ----------------------------

    follow_up_map = {
        "High": "2 Hours",
        "Medium": "24 Hours",
        "Low": "3 Days"
    }

    follow_up = follow_up_map.get(urgency, "24 Hours")

    # ----------------------------
    # Workflow Actions
    # ----------------------------

    actions = [
        "Complaint received",
        "Acknowledgement sent to customer",
        f"Assigned to {assigned_team}",
        "Case logged into audit system",
        f"Follow-up scheduled ({follow_up})"
    ]

    if category == "billing":
        actions.extend([
            "Verify transaction history",
            "Check for duplicate billing",
            "Initiate refund if required"
        ])

    elif category == "technical":
        actions.extend([
            "Collect diagnostic information",
            "Create engineering support ticket",
            "Notify customer after investigation"
        ])

    elif category == "security":
        actions.extend([
            "Temporarily secure customer account",
            "Notify Security Operations",
            "Start fraud investigation"
        ])

    elif category == "delivery":
        actions.extend([
            "Contact logistics partner",
            "Track shipment",
            "Provide delivery update"
        ])

    elif category == "account":
        actions.extend([
            "Verify customer identity",
            "Review account details",
            "Resolve account-related issue"
        ])

    else:
        actions.append("Investigate complaint and provide resolution")

    # ----------------------------
    # Draft Customer Response
    # ----------------------------

    draft_response = f"""
Dear Customer,

Thank you for contacting us.

We have received your complaint and sincerely apologize for the inconvenience.

Your request has been assigned to our {assigned_team} for investigation.

Priority: {urgency}
Expected Follow-up: {follow_up}

We appreciate your patience and will keep you updated throughout the resolution process.

Regards,

Customer Support Team
"""

    return {
        "assigned_team": assigned_team,
        "priority": urgency,
        "status": "Open",
        "follow_up": follow_up,
        "actions": actions,
        "draft_response": draft_response
    }