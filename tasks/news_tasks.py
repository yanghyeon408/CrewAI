from crewai import Task

def create_news_tasks(news_collector, news_organizer, news_summarizer):
    collect_task = Task(
        description="""Search for the latest Tesla and Elon Musk news from the past 24 hours.
        Focus on:
        - Official Tesla announcements and press releases
        - Financial news and stock market updates
        - Product development and technology news
        - Manufacturing and production updates
        - Regulatory and legal developments
        - Elon Musk's public statements and activities
        
        Gather comprehensive information from reliable sources including major news outlets,
        financial publications, and official Tesla communications.""",
        agent=news_collector,
        expected_output="A comprehensive list of recent Tesla and Elon Musk news articles with URLs, headlines, and brief descriptions."
    )
    
    organize_task = Task(
        description="""Analyze and organize the collected Tesla news by:
        1. Filtering for relevance and credibility
        2. Removing duplicate stories
        3. Categorizing by topic (financial, product, legal, etc.)
        4. Ranking by importance and potential impact
        5. Identifying breaking news vs. routine updates
        
        Focus on news that could significantly impact Tesla's business, stock price, or industry position.""",
        agent=news_organizer,
        expected_output="An organized list of Tesla news categorized by topic and ranked by importance, with duplicates removed."
    )
    
    summarize_task = Task(
        description="""Create a comprehensive daily summary of Tesla and Elon Musk news including:
        
        1. Stock Price: Current Tesla stock price and market performance
        2. Executive Summary: Key highlights and major developments
        3. Financial Impact: News affecting stock price or business performance
        4. Product & Technology: Updates on vehicles, software, and innovations
        5. Operations: Manufacturing, production, and business operations
        6. Leadership & Strategy: Elon Musk's statements and strategic decisions
        7. Market & Industry: Competitive landscape and industry developments
        
        Each section should include:
        - Key points and implications
        - Potential impact on Tesla's business
        - Context and background information
        - Source credibility assessment
        
        Write in a professional, objective tone suitable for investors and industry professionals.""",
        agent=news_summarizer,
        expected_output="A detailed daily summary report of Tesla news organized by categories with analysis and implications."
    )

    # translate_task = Task(
    #     description="""Translate the comprehensive Tesla news summary into Korean.
    #     Ensure that technical terms are accurately translated and provide context where necessary.
    #     The translation should maintain the original meaning while making the content accessible to a Korean-speaking audience.""",
    #     agent=news_translator,
    #     expected_output="A clear, concise Korean translation of the Tesla news summary."
    # )
    
    return [collect_task, organize_task, summarize_task]