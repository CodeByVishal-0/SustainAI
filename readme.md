# 🌱 SustainAI - Multi-Agent Sustainability Intelligence Platform

SustainAI is an AI-powered sustainability analysis platform that combines Retrieval-Augmented Generation (RAG), real-time environmental data, news intelligence, and Large Language Models to generate sustainability reports for cities.

The platform analyzes environmental conditions, sustainability knowledge, and current news to provide actionable recommendations aligned with the United Nations Sustainable Development Goals (SDGs).

---

## 🚀 Features

### 📚 RAG-Based Sustainability Knowledge Base

* Loads sustainability and SDG documents
* Generates embeddings using Hugging Face
* Stores vectors in ChromaDB
* Retrieves relevant sustainability insights

### 🤖 AI-Powered Question Answering

* Uses Groq Llama 3 for response generation
* Answers sustainability-related questions using retrieved context

### 🌦️ Weather Intelligence Agent

* Fetches real-time weather data
* Retrieves Air Quality Index (AQI)
* Analyzes environmental conditions

### 📰 News Intelligence Agent

* Collects city-specific environmental news
* Tracks pollution, climate, and sustainability-related developments

### 📊 Sustainability Impact Agent

* Calculates sustainability score
* Determines environmental risk level
* Generates sustainability recommendations

### 🎯 Orchestrator Agent

* Coordinates all agents
* Combines:

  * Weather Analysis
  * AQI Analysis
  * News Intelligence
  * RAG Insights
  * LLM Reasoning

### ⚡ FastAPI Backend

* REST API architecture
* Swagger UI documentation
* Structured JSON responses

---

## 🏗️ System Architecture

User Query

↓

FastAPI Backend

↓

Orchestrator Agent

├── Weather Agent

├── News Agent

├── Impact Agent

└── RAG Agent

↓

ChromaDB + HuggingFace Embeddings

↓

Groq Llama 3

↓

Sustainability Report

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python
* Uvicorn

### AI & LLM

* Groq Llama 3
* LangChain

### Vector Database

* ChromaDB

### Embeddings

* HuggingFace Embeddings
* all-MiniLM-L6-v2

### APIs

* OpenWeather API
* GNews API

### Data Processing

* PyPDFDirectoryLoader
* RecursiveCharacterTextSplitter

---

## 📂 Project Structure

```text
SustainAI/
│
├── agents/
│   ├── rag_agent.py
│   ├── weather_agent.py
│   ├── news_agent.py
│   ├── impact_agent.py
│   └── orchestrator.py
│
├── utils/
│   ├── embedding.py
│   ├── vector_store.py
│   ├── weather_api.py
│   ├── news_api.py
│   └── llm.py
│
├── schemas/
│   ├── request_models.py
│   └── response_models.py
│
├── routers/
│   └── sustainability.py
│
├── data/
│
├── chroma_db/
│
├── main.py
├── ingest.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SustainAI.git
cd SustainAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
GNEWS_API_KEY=your_gnews_api_key
```

---

## 📥 Load Documents

Place sustainability PDFs inside:

```text
data/
```

Generate vector embeddings:

```bash
python ingest.py
```

---

## ▶️ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoint

### Analyze Sustainability

```http
POST /api/analyze
```

Request:

```json
{
  "city": "Mumbai",
  "question": "How sustainable is Mumbai today?"
}
```

Response:

```json
{
  "city": "Mumbai",
  "weather": {},
  "impact": {},
  "news": [],
  "rag_insights": "...",
  "report": "..."
}
```

---

## 🎯 Sustainable Development Goals (SDGs)

Current knowledge base includes:

* SDG 11 – Sustainable Cities and Communities
* SDG 12 – Responsible Consumption and Production
* SDG 13 – Climate Action

---

## 🔮 Future Enhancements

* React + Tailwind Frontend
* LangGraph Agent Workflow
* Sustainability Dashboard
* Historical Trend Analysis
* Carbon Footprint Estimation
* Multi-City Comparison
* Deployment on Render & Vercel

---

## 👨‍💻 Author

Vishal

Built as part of an AI for Sustainability initiative using Multi-Agent AI Systems, RAG, ChromaDB, FastAPI, and Groq.
