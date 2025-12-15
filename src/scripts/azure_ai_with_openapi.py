# Copyright (c) Microsoft. All rights reserved.
import asyncio
import json
from pathlib import Path

import aiofiles
from agent_framework.azure import AzureAIClient
from azure.identity.aio import AzureCliCredential

"""
Azure AI Agent with OpenAPI Tool Example

This sample demonstrates usage of AzureAIClient with OpenAPI tools
to call external APIs defined by OpenAPI specifications.

Prerequisites:
1. Set AZURE_AI_PROJECT_ENDPOINT and AZURE_AI_MODEL_DEPLOYMENT_NAME environment variables.
2. The countries.json OpenAPI specification is included in the resources folder.
"""


async def main() -> None:
    # Load the OpenAPI specification
    resources_path = Path(__file__).parent.parent / "resources" / "user-finance-api.json"

    async with aiofiles.open(resources_path, "r") as f:
        content = await f.read()
        openapi = json.loads(content)

    async with (
        AzureCliCredential() as credential,
        AzureAIClient(credential=credential).create_agent(
            name="MyOpenAPIAgent",
            instructions="""you are a finance asistant.

you only goal is to provide guidance to a user about his debts, to this purpose you must use the tool debtAnalysisAPI wich will allow you to fetch information of a specific product from a user.

To use this tool always ask the user for the customer_id and product_type wich then you will use to call the tool API

Analize the response and offer a neat resume and provide guidance so the user can make the best possible choice""",
            tools={
                "type": "openapi",
                "openapi": {
                    "name": "debtAnalysisAPI",
                    "spec": openapi,
                    "description": "Retrieve information about a user's debt products",
                    "auth": {"type": "anonymous"},
                },
            },
        ) as agent,
    ):
        query = "Run an anlysis of the debts for the customer with id CU-001 and product type loan."
        print(f"User: {query}")
        result = await agent.run(query)
        print(f"Agent: {result}\n")


if __name__ == "__main__":
    asyncio.run(main())