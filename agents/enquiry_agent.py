def process_enquiry(request: str, classification: dict):
    """
    Process a general enquiry and generate a remediation workflow.
    """

    category = classification.get("category", "General").lower()

    # ----------------------------
    # Determine responsible team
    # ----------------------------

    if category == "account":
        assigned_team = "Account Support"

    elif category == "billing":
        assigned_team = "Billing Helpdesk"

    elif category == "technical":
        assigned_team = "Technical Support"

    elif category == "payment":
        assigned_team = "Finance Helpdesk"

    else:
        assigned_team = "AI Knowledge Base"

    # ----------------------------
    # Workflow Actions
    # ----------------------------

    actions = [
        "Enquiry received",
        "Knowledge base searched",
        "Relevant information retrieved",
        "AI response generated",
        "Case marked as resolved"
    ]

    draft_response = f"""
Dear Customer,

Thank you for contacting us.

Based on your enquiry, we have generated the most relevant response using our knowledge base.

If your question requires further assistance, it has been routed to our {assigned_team}.

Regards,

Customer Support Team
"""

    return {
        "assigned_team": assigned_team,
        "priority": "Low",
        "status": "Resolved",
        "follow_up": "Not Required",
        "actions": actions,
        "draft_response": draft_response
    }