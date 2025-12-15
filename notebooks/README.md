# Azure AI Agent with OpenAPI Tools (Python Notebook)

This repository contains a **Jupyter Notebook** that creates and executes a test run of a **Azure AI Agent** using **OpenAPI tools**, based on the official Microsoft Azure AI Agent Framework example.

The agent uses an OpenAPI specification (`user-finance-api.json`) to call an external API and answer questions about countries, currencies, and demographics.

---

## Why is it necessary?

- The execution of the notebook creates a agent in Azure AI Foundry allowing the API `finance-ai-agent`to run properly
- The notebook takes into account all the needed parameters for the correct creation and execution of the agent

---

## 🧠 Use Case Example

The agent can answer questions like:

> *"Dame informacion del cliente CU-001 con producto de tipo loan"*

It automatically decides when to call the OpenAPI tool and uses the response to generate an answer.

---