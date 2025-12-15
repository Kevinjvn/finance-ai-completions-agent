import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration"""

    # Azure Storage settings
    AI_FOUNDRY_ENDPOINT = os.getenv("AI_FOUNDRY_ENDPOINT")
    AI_AGENT_NAME = os.getenv("AI_AGENT_NAME")

    @classmethod
    def validate(cls):
        """Validate required configuration"""
        if not cls.AI_FOUNDRY_ENDPOINT:
            raise ValueError("AI_FOUNDRY_ENDPOINT environment variable is required")
        
        if not cls.AI_AGENT_NAME:
            raise ValueError("AI_AGENT_NAME environment variable is required")
