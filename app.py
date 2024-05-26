from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import your classes and functions from the provided code
from rag.components.get_response import GetChatResponse, GetChainResponse

# Initialize FastAPI app
app = FastAPI()

# Define CORS settings
origins = ["*"]  # You can specify origins here or set it to "*" to allow all origins

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Define request body models using Pydantic
class QuestionRequest(BaseModel):
    question: str

# Initialize instances of your classes
chat_response = GetChatResponse("https://en.wikipedia.org/wiki/Luke_Skywalker")
chain_response = GetChainResponse("https://en.wikipedia.org/wiki/Luke_Skywalker")


@app.get("/")
async def read_root():
    return FileResponse("frontend/index.html")

# Define endpoint for getting chat response
@app.post("/chat/response")
async def get_chat_response(request_data: QuestionRequest):
    try:
        response = chat_response.get_response(request_data.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define endpoint for getting chain response
@app.post("/chain/response")
async def get_chain_response(request_data: QuestionRequest):
    try:
        response = chain_response.get_response(request_data.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
