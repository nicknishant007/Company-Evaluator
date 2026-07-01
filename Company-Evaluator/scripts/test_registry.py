from llms.factory import LLMFactory

from agents.registry import (
    AgentRegistry,
)


llm = LLMFactory.get_llm()

registry = AgentRegistry(
    llm
)

print(
    registry.agents.keys()
)