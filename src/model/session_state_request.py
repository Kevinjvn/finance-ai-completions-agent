"""
This module defines the SessionStateRequest model, which represents a request to manage the session state,
including an optional thread ID for identifying the conversation.
"""

from typing import Optional

from pydantic import BaseModel, Field


class SessionStateRequest(BaseModel):
    """
    Represents a request to manage the session state, including an optional thread ID for the conversation.
    """

    threadId: Optional[str] = Field(
        None,
        description="Identificador único del hilo de conversación generado por Azure Foundry",
        json_schema_extra={"example": "thread_rrdnmO3xTJobugSetrR2y76t"},
    )
