from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient

from src.config import Config
import logging

logger = logging.getLogger(__name__)


class AIFoundryClients:
    """Singleton container for Azure AI Foundry clients"""

    def __init__(self):
        self._credential: DefaultAzureCredential | None = None
        self._project_client: AIProjectClient | None = None

    async def initialize(self):
        """Initialize all clients (call once at startup)"""
        if self._credential is None:
            self._credential = DefaultAzureCredential()
            logger.info("DefaultAzureCredential initialized")

        if self._project_client is None:
            self._project_client = AIProjectClient(
                endpoint=str(Config.AI_FOUNDRY_ENDPOINT),
                credential=self._credential,
            )
            logger.info("AIProjectClient initialized")

    async def close(self):
        """Close all clients (call once at shutdown)"""
        if self._project_client:
            await self._project_client.close()
            self._project_client = None
            logger.info("AIProjectClient closed")

        if self._credential:
            await self._credential.close()
            self._credential = None
            logger.info("DefaultAzureCredential closed")

    @property
    def credential(self) -> DefaultAzureCredential:
        if self._credential is None:
            raise RuntimeError("Clients not initialized. Call initialize() first.")
        return self._credential

    @property
    def project_client(self) -> AIProjectClient:
        if self._project_client is None:
            raise RuntimeError("Clients not initialized. Call initialize() first.")
        return self._project_client


# Global singleton instance
ai_clients = AIFoundryClients()
