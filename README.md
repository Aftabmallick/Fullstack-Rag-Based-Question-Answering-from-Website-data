# Conversational RAG

This repository contains a FastAPI backend and HTML, CSS Frontend that provides endpoints for interacting with a RAG conversational system. It allows users to send questions and receive responses based on a Luke Skywalker Wikipedia Data.

## Installation

1. Open project folder:

```bash
cd assignment_2
```

2. Create ".env" file:

```bash
OPENAI_API_KEY = "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxx"
```

3. Create virtual environment:
```bash
python -m venv venv
venv/scripts/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The server will start running at `http://localhost:8000` by default. Start Chat about Luke Sky walker




