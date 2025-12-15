# Copyright (c) Microsoft. All rights reserved.

import asyncio
import os

from agent_framework import ChatAgent
from agent_framework.azure import AzureAIAgentClient
from azure.ai.agents.aio import AgentsClient
from azure.identity.aio import DefaultAzureCredential

"""
Azure AI Agent with Existing Agent Example

This sample demonstrates working with pre-existing Azure AI Agents by providing
agent IDs, showing agent reuse patterns for production scenarios.
"""


async def main() -> None:
    print("=== Azure AI Chat Client with Existing Agent ===")

    # Create the client
    async with (
        DefaultAzureCredential() as credential,
        AgentsClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"], credential=credential) as agents_client,
    ):
        chat_client = AzureAIAgentClient(agents_client=agents_client, agent_name="assistant")

        try:
            async with ChatAgent(
                chat_client=chat_client,
                # Instructions here are applicable only to this ChatAgent instance
                # These instructions will be combined with instructions on existing remote agent.
                # The final instructions during the execution will look like:
                # "'End each response with [END]. Respond with 'Hello World' only'"
                # instructions="Respond with 'Hello World' only",
            ) as agent:
                thread = agent.get_new_thread()
                query = "mi nombre es kevin"
                print(f"User: {query}")
                result = await agent.run(query, thread=thread)
                # Based on local and remote instructions, the result will be
                # 'Hello World [END]'.
                print(f"Agent: {result}\n")

                query2 = "Cual era mi nombre?"
                print(f"User: {query2}")
                result = await agent.run(query2, thread=thread)
                print(f"Agent: {result}\n")
        finally:
            # Clean up the agent manually
            # await agents_client.delete_agent(azure_ai_agent.id)
            print("Demo complete.")


if __name__ == "__main__":
    asyncio.run(main())