"""
This module defines the ChatRequest model, which represents the structure of a chat request, including messages,
optional context, and session state.
"""

from typing import List, Optional

from pydantic import BaseModel, Field

from src.model.context_request import ContextRequest
from src.model.message_request import MessageRequest
from src.model.session_state_request import SessionStateRequest


class ChatRequest(BaseModel):
    """
    Represents a chat request, including a list of messages, optional context, and session state.
    """

    messages: List[MessageRequest] = Field(
        ...,
        description="Lista de mensajes en el formato del protocolo Chat AI",
        json_schema_extra={"maxItems": 10}
    )
    context: Optional[ContextRequest] = Field(default=None)
    sessionState: Optional[SessionStateRequest] = Field(default=None)
