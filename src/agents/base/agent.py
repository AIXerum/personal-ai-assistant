from typing import List
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from src.utils import get_llm_by_provider

class Agent:
    def __init__(
        self, 
        name: str,  # Name of the agent
        description: str,  # Description of the agent (a brief explanation of its function or purpose)
        system_prompt: str,  # The instructions for the agent
        tools: List[str],  # List of tools that the agent can use
        sub_agents: List['Agent'],  # List of sub-agents that the main agent can sned message to
        model: str,  # LLM model (in provider/model format e.g., "openai/gpt-4o", "gemini/gemini-1.5-flash")
        temperature: float  # Temperature setting for the LLM (affects creativity/randomness)

    ):
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.tools = tools
        self.sub_agents = sub_agents
        self.model = model
        self.temperature = temperature
        self.agent = None 
        self.memory = MemorySaver()

    def invoke(self, *args, **kwargs):
        if not self.agent:
            self.initiat_agent()
        
        response = self.agent.invoke(*args, **kwargs)
        return response
    
    def stream(self, *args, **kwargs):
        if not self.agent:
            self.initiat_agent()
        
        for chunk in self.agent.stream(*args, **kwargs):
            yield chunk

    def initiat_agent(self):
        llm = get_llm_by_provider(self.model, self.temperature)
        self.memory = MemorySaver()
        self.agent = create_react_agent(
            llm, 
            tools=self.tools, 
            checkpointer=self.memory,
            state_modifier=self.system_prompt
        )
