import logging

from azure.ai.projects.aio import AIProjectClient
from fastapi.responses import JSONResponse

from src.config import Config
from src.model.chat_request import ChatRequest
from src.model.chat_response import ChatResponse
from src.model.message_response import MessageResponse

logger = logging.getLogger(__name__)


async def call_ai_agent(
    request: ChatRequest, project_client: AIProjectClient
) -> ChatResponse | JSONResponse:
    """
    Calls the AI agent with the provided chat request and returns the chat response.

    Args:
        request (ChatRequest): The chat request containing messages, context, and session state.

    Returns:
        ChatResponse: The response from the AI agent.
    """
    try:
        # Get an existing agent
        agent = await project_client.agents.get(agent_name=str(Config.AI_AGENT_NAME))
        logger.info(f"Retrieved agent: {agent.name}")

        openai_client = project_client.get_openai_client()

        user_message = request.messages[0]
        user_text = user_message.content

        # Reference the agent to get a response
        response = await openai_client.responses.create(
            input=[{"role": "user", "content": user_text}],
            extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
        )

        logger.info(response.conversation)

        return ChatResponse(
            message=MessageResponse(content=response.output_text, role="assistant")
        )
    except Exception as e:
        logger.error(f"Error calling AI agent: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
