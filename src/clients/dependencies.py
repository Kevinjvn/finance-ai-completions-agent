from agent_framework import ChatAgent
from fastapi import Request


def get_project_client(request: Request):
    return request.app.state.project_client
