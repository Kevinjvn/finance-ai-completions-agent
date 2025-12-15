"""
This module defines models for handling context responses, including follow-up questions and related data points
such as texts or links.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class DataPoints(BaseModel):
    """
    Represents a collection of related texts or links associated with the agent's response.
    """

    text: Optional[set[str]] = Field(
        default_factory=set,
        description="Lista de textos o enlaces relacionados con la respuesta del agente",
    )


class ContextResponse(BaseModel):
    """
    Represents the response for a context request, including follow-up questions and additional data points.
    """

    followup_questions: Optional[List[str]] = Field(default_factory=list)
    data_points: Optional[DataPoints] = Field(
        None,
        description="Información adicional proporcionada por el agente, incluyendo enlaces a documentos",
    )
