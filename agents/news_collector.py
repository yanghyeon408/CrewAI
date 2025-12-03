from crewai import Agent
from crewai.tools import tool
from duckduckgo_search import DDGS
from config.llm_config import llama_llm

@tool("DuckDuckGo Search")
def search_web(query: str) -> str:
    """무료 웹 검색"""
    ddgs = DDGS()
    results = ddgs.text(keywords=query, max_results=3)
    
    formatted = []
    for i, result in enumerate(results, 1):
        formatted.append(f"{i}. {result['title']}\n   {result['body'][:100]}...")
    
    return '\n\n'.join(formatted)

news_collector = Agent(
    role="Tesla News Collector",
    goal="Collect the latest news about Tesla and Elon Musk from various sources",
    backstory="""You are a skilled news researcher specializing in Tesla and Elon Musk coverage.
    You have a keen eye for finding relevant, up-to-date news from reliable sources including
    financial news, tech blogs, automotive industry publications, and official Tesla announcements.
    Also collect Tesla's stock price and market performance data from financial news sites.""",
    tools=[search_web],
    verbose=True,
    allow_delegation=False,
    llm=llama_llm
)