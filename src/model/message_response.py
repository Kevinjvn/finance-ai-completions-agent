"""
This module defines the MessageResponse model, which represents the structure of a response message, including
the content and the sender's role.
"""

from typing import Optional

from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    """
    Represents the response for a message, including the content and the optional role of the sender.
    """

    content: str = Field(
        ...,
        min_length=1,
    )
    role: Optional[str] = Field(
        None,
        description="Rol relacionado al cliente que realiza la petición.",
    )
