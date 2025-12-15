"""
This module defines the ChatResponse model, which represents the structure of a chat response, including the message,
optional context, and session state.
"""

from typing import Optional

from pydantic import BaseModel

from src.model.context_response import ContextResponse
from src.model.message_response import MessageResponse
from src.model.session_state_response import SessionStateResponse


class ChatResponse(BaseModel):
    """
    Represents the response for a chat request, including the message, optional context, and session state.
    """

    message: MessageResponse
    context: Optional[ContextResponse] = None
    sessionState: Optional[SessionStateResponse] = None
