"""
This module defines the ContextRequest model, which specifies the structure for requests to retrieve context
from a search engine.
"""

from typing import Optional

from pydantic import BaseModel, Field


class ContextRequest(BaseModel):
    """
    Represents a request for context, specifying the number of search results to retrieve.
    """

    top: Optional[int] = Field(
        default=None,
        description="Número de resultados a retornar del motor de búsqueda.",
        json_schema_extra={"example": 3},
    )
