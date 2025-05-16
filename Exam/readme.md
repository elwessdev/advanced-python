# 🎬 LLM-Powered Movie & Actor Explorer

A two-part system that combines **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Langchain + Groq**, and **Streamlit** to let users explore movie data and generate LLM-based summaries.

---

## 🚀 Objective

This project demonstrates full-stack integration of:
- **FastAPI** backend with relational models (Movies ↔ Actors)
- **PostgreSQL** via **SQLAlchemy** ORM relationships
- **Pydantic** models for validation and response
- **Langchain (Groq)** for dynamic text generation
- **Streamlit** frontend for user-friendly interaction

---

## 📦 Components

### 1. **FastAPI Backend**
- Add and retrieve movie + actor data
- Serve random movies and their actors
- Generate LLM-based summaries (Langchain with Groq)
- Swagger UI: `http://localhost:8000/docs`

### 2. **Streamlit Frontend**
- Display random movie with its actors
- Request movie summaries via LLM
- Clean, interactive UI using API endpoints

---

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Langchain + Groq
- Streamlit

---

## ▶️ Getting Started

```bash
# 1. Create virtual environment
python3.10 -m venv .venv && source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FastAPI backend
uvicorn main_fastapi:app --reload

# 4. Run Streamlit frontend
streamlit run main_streamlit.py
