"""
This module defines the MessageRequest model, which represents the structure of a message request, including the
sender's role and the message content.
"""

from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    """
    Represents a message request, including the role of the sender and the content of the message.
    """

    role: str = Field(
        ...,
        description="Rol relacionado al cliente que realiza la petición.",
        json_schema_extra={"example": "user"},
    )
    content: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Mensaje y/o solicitud del usuario.",
        json_schema_extra={"example": "Hello"},
    )
