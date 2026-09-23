# 📝 AI Customer Feedback Analyzer

An AI-powered customer feedback analyzer built with Python, Streamlit, FastAPI, SQLite, and the Gemini API.

The application allows a business owner to paste multiple customer reviews, analyze them using Gemini, and view the sentiment, rating, and main theme of each review.

---

## 🚀 Features

- Analyze multiple customer reviews at once
- Classify reviews as:
  - Positive
  - Negative
  - Neutral
- Generate a 1–5 score for each review
- Identify the main theme of each review
- Display results in a structured table
- Calculate:
  - Total number of reviews
  - Average score
  - Percentage of positive reviews
- Identify the most frequently mentioned theme
- Save analyzed reviews to a local SQLite database
- View previously saved reviews
- FastAPI backend separated from the Streamlit frontend
- Structured AI responses using Pydantic

---

## 🛠️ Tech Stack

### Frontend
- Python
- Streamlit

### Backend
- FastAPI
- Pydantic
- Requests

### AI
- Google Gemini API
- Google GenAI Python SDK

### Database
- SQLite

### Development
- uv
- Git / GitHub

---

## 🏗️ Project Architecture

```text
                  ┌─────────────────────┐
                  │     Streamlit UI    │
                  │       app.py        │
                  └──────────┬──────────┘
                             │
                             │ HTTP POST
                             ▼
                  ┌─────────────────────┐
                  │     FastAPI API     │
                  │       api.py        │
                  └──────────┬──────────┘
                             │
                             │ Gemini API
                             ▼
                  ┌─────────────────────┐
                  │    Google Gemini    │
                  └─────────────────────┘

                  ┌─────────────────────┐
                  │      SQLite DB      │
                  │    database.py      │
                  └─────────────────────┘
