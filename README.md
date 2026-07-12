# 🤖 Agentic AI Customer Request Processing System

An AI-powered customer support automation system that classifies customer requests, routes them to specialized workflow agents, automates remediation workflows, persists request history, and provides an operational dashboard.

This project demonstrates an **Agentic AI workflow** where an LLM performs intelligent request classification and a router dispatches requests to dedicated agents for workflow execution.

---

## Features

- AI-powered request classification using **Google Gemini**
- Intelligent routing to specialized workflow agents
- Complaint workflow automation
- Service Request workflow automation
- General Enquiry workflow automation
- Confidence score and reasoning for AI decisions
- SQLite-based persistence
- Interactive Streamlit dashboard
- Sample requests for quick testing

---

## Architecture

```
                    Customer Request
                           │
                           ▼
                  Streamlit User Interface
                           │
                           ▼
                 Gemini AI Request Classifier
                           │
         ┌─────────────────┴─────────────────┐
         │                                   │
      Router Agent (Intent Routing)
         │
 ┌───────┼───────────────┐
 │       │               │
 ▼       ▼               ▼
Complaint Service      Enquiry
 Agent     Agent         Agent
 │          │             │
 └──────────┼─────────────┘
            │
            ▼
      SQLite Persistence
            │
            ▼
     Analytics Dashboard
```

---

## Project Structure

```
agentic-ai-request-processor/
│
├── app.py
├── llm.py
├── database.py
├── requirements.txt
├── sample_requests.json
├── README.md
│
├── agents/
│   ├── complaint_agent.py
│   ├── service_agent.py
│   └── enquiry_agent.py
│
├── pages/
│   └── dashboard.py
│
└── data/
    └── logs.db
```

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- SQLite
- Pandas

---

## Workflow

1. User submits a customer request.
2. Gemini AI classifies the request into:
   - Complaint
   - Service Request
   - General Enquiry
3. The Router Agent forwards the request to the appropriate workflow agent.
4. The selected agent:
   - assigns the responsible team,
   - determines priority,
   - creates remediation actions,
   - generates a draft customer response.
5. The processed request is stored in SQLite.
6. The Dashboard displays request history and analytics.

---

## Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd agentic-ai-request-processor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file.

```
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Sample Requests

### Complaint

```
I was charged twice for my credit card payment.
Please refund immediately.
```

Expected:

- Category: Complaint
- Team: Billing Support
- Status: Open

---

### Service Request

```
Please update my registered mobile number.
```

Expected:

- Category: Service Request
- Team: Customer Operations
- Status: In Progress

---

### General Enquiry

```
How do I reset my password?
```

Expected:

- Category: General Enquiry
- Team: AI Knowledge Base / Account Support
- Status: Resolved

---

## Dashboard

The analytics dashboard provides:

- Total Requests
- Complaint Count
- Service Request Count
- General Enquiry Count
- Request History
- Category Distribution
- Urgency Distribution

---

## AI Classification Output

Gemini returns structured JSON.

Example:

```json
{
  "label": "Complaint",
  "category": "Billing",
  "urgency": "High",
  "confidence": 98,
  "reason": "Customer reports duplicate billing."
}
```

---

## Future Enhancements

- PostgreSQL integration
- FastAPI backend
- LangGraph-based multi-agent orchestration
- Human-in-the-loop approvals
- Authentication and RBAC
- Cloud deployment
- Email/Slack notifications
- Monitoring and observability

---

## Design Decisions

### Why Gemini?

Gemini provides fast inference, structured JSON generation, and excellent support for prompt-based request classification, making it suitable for rapidly building an AI-powered prototype.

### Why Specialized Agents?

Different request types require different business workflows. Separating the logic into Complaint, Service, and Enquiry agents improves modularity, maintainability, and scalability.

### Why SQLite?

SQLite provides lightweight persistence without external infrastructure while maintaining an audit trail of processed requests.

### Why Streamlit?

Streamlit enables rapid development of an interactive interface suitable for demonstrations and internal tools.

---

## Future Production Architecture

```
Users
   │
Load Balancer
   │
FastAPI
   │
Gemini
   │
Router Agent
   │
Workflow Agents
   │
PostgreSQL
   │
Analytics Dashboard
```

---

## Author

**Vinay Maryala**
