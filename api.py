"""
The backend: a small FastAPI service that analyzes ONE customer review.

Run it with:
    uv run fastapi dev api.py
    OR
    fastapi run api.py

Then the Streamlit app (app.py) will call this service for every review.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

app = FastAPI()


# What the caller must SEND us
class Review(BaseModel):   # pydantic class
    text: str


# What Gemini gives back, and what we SEND to the caller.
# We keep it small on purpose -> fewer tokens used.
class Analysis(BaseModel):
    label: str   # "positive", "negative", or "neutral"
    score: int   # 1 (very bad) to 5 (very good)
    theme: str   # one word: what the review is mainly about (e.g. "delivery")
    suggestion: str 


@app.post("/analyze")
def analyze(review: Review):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=(
            "Analyze this customer review.\n"
            "label must be 'positive', 'negative', or 'neutral'.\n"
            "score must be a number from 1 (very bad) to 5 (very good).\n"
            "theme must be ONE lowercase word for the main topic "
            "(for example: delivery, taste, price, service, quality).\n"
            "suggestion must be a short one-line suggestion for improving the "
            "business IF the review is negative. For positive or neutral reviews, "
            "suggestion must be 'None'.\n"
            f"Review: {review.text}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Analysis,      # give output in this schema
        ),
    )
    return response.parsed
