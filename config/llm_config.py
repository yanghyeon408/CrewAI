from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    """
    Configure and return LLM instance
    Options: ollama, openai, groq, openrouter
    """
    llm_provider = os.getenv("LLM_PROVIDER", "ollama").lower()
    
    if llm_provider == "ollama":
        return LLM(
            model="ollama/llama3.1",
            base_url="http://localhost:11434"
        )
    
    elif llm_provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        return LLM(
            model="gpt-4o-mini",
            api_key=api_key
        )
    
    elif llm_provider == "groq":
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        return LLM(
            model="groq/llama-3.1-70b-versatile",
            api_key=api_key
        )
    
    elif llm_provider == "openrouter":
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        return LLM(
            model="qwen/qwen-2.5-72b-instruct",
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )
    
    else:
        raise ValueError(f"Unsupported LLM provider: {llm_provider}")

# Get the configured LLM instance
llama_llm = get_llm()