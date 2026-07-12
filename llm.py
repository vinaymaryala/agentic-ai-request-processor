import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def classify_request(user_request: str) -> dict:

    prompt = f"""
You are an enterprise AI request classification system.

Analyze the customer request and return ONLY valid JSON.

Choose:

Label:
- Complaint
- Service Request
- General Enquiry

Category:
- Billing
- Technical
- Account
- Security
- Delivery
- Maintenance
- Profile Update
- Payment
- General

Urgency:
- High
- Medium
- Low

Confidence:
0-100

Reason:
Short explanation.

Return JSON exactly like this:

{{
    "label":"Complaint",
    "category":"Billing",
    "urgency":"High",
    "confidence":<integer between 0 and 100>,
    "reason":"Customer reports duplicate billing."
}}

Customer Request:

{user_request}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini returns ```json
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)