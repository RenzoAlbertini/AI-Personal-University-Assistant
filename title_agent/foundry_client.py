import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from dotenv import load_dotenv
load_dotenv()

class FoundryClient:
    """Azure Foundry OpenAI client wrapper for study plan generation."""

    def __init__(self):
        """Initialize Foundry client with Azure identity credentials."""
        # Get Azure credentials (requires 'az login')
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://ai.azure.com/.default"
        )

        # Configure Foundry agent endpoint
        api_version = os.getenv("FOUNDRY_API_VERSION", "v1")

        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("FOUNDRY_AGENT_ENDPOINT"),
            azure_ad_token_provider=token_provider,
            api_version=api_version
        )

    def run(self, message: str) -> str:
        """Send message to Foundry agent and return text response."""
        response = self.client.responses.create(
            model="agente",  # Foundry agent endpoint name
            input=message
        )

        return response.output_text