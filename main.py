import os
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process

from agents.news_collector import news_collector
from agents.news_organizer import news_organizer
from agents.news_summarizer import news_summarizer
from agents.news_translator import news_translator
from tasks.news_tasks import create_news_tasks

load_dotenv()

def main():
    print("🚗 Tesla News Scraper with CrewAI")
    print("=" * 50)
    
    llm_provider = os.getenv("LLM_PROVIDER", "ollama")
    print(f"🤖 Using LLM provider: {llm_provider}")
    
    if llm_provider == "openai" and not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please copy .env.example to .env and add your API keys")
        return
    elif llm_provider == "groq" and not os.getenv("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY not found in environment variables") 
        print("Please copy .env.example to .env and add your API keys")
        return
    
    
    tasks = create_news_tasks(news_collector, news_organizer, news_summarizer)
    
    crew = Crew(
        agents=[news_collector, news_organizer, news_summarizer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    print(f"🔍 Starting Tesla news collection for {datetime.now().strftime('%Y-%m-%d')}")
    
    try:
        result = crew.kickoff()
        
        output_file = f"output/tesla_news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Tesla Daily News Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(str(result))
        
        print(f"✅ News summary saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error during news collection: {str(e)}")
        print("Please check your API keys and internet connection")

if __name__ == "__main__":
    main()