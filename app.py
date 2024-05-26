from fastapi import FastAPI, HTTPException
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
class WebsiteInput(BaseModel):
    website_url: str

class QuestionRequest(BaseModel):
    question: str

# Initialize instances of your classes
chat_response = None
chain_response = None

@app.get("/")
async def read_root():
    return FileResponse("frontend/index.html")

# Define endpoint to set website URL and initiate chat
@app.post("/initiate_chat")
async def initiate_chat(website_input: WebsiteInput):
    global chat_response, chain_response
    try:
        chat_response = GetChatResponse(website_input.website_url)
        chain_response = GetChainResponse(website_input.website_url)
        return {"message": "Chat initiated successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define endpoint for getting chat response
@app.post("/chat/response")
async def get_chat_response(request_data: QuestionRequest):
    if chat_response is None:
        raise HTTPException(status_code=400, detail="Chat not initiated. Please set website URL first.")
    try:
        response = chat_response.get_response(request_data.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define endpoint for getting chain response
@app.post("/chain/response")
async def get_chain_response(request_data: QuestionRequest):
    if chain_response is None:
        raise HTTPException(status_code=400, detail="Chat not initiated. Please set website URL first.")
    try:
        response = chain_response.get_response(request_data.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
