"""Azure AI Foundry Study Planner Agent module.

This module provides A2A-compatible agent implementation for generating
personalized study plans using Microsoft Azure Foundry and the gpt-4.1 model.
"""

__version__ = "1.0.0"
__author__ = "Microsoft Learning"

from title_agent.agent_executor import FoundryAgentExecutor
from title_agent.foundry_client import FoundryClient
from title_agent.server import app

__all__ = ["FoundryAgentExecutor", "FoundryClient", "app"]
