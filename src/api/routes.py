from azure.ai.projects.aio import AIProjectClient
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.clients.dependencies import get_project_client
from src.core.ai_chat import call_ai_agent
from src.model.chat_request import ChatRequest
from src.model.chat_response import ChatResponse

router = APIRouter(prefix="/api", tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    project_client: AIProjectClient = Depends(get_project_client),
):
    try:
        return await call_ai_agent(request, project_client)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
