# Tesla News Scraper

A Python-based news aggregation system that uses CrewAI to collect, organize, and summarize Tesla-related news articles.

## Features

- Automated Tesla news collection from multiple sources
- AI-powered news organization and summarization
- Support for multiple LLM providers (OpenAI, Groq, Ollama)
- Daily news summaries saved to output files

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd TESLA
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys for your preferred LLM provider

## Usage

Run the news scraper:
```bash
python main.py
```

The application will:
- Collect Tesla news from various sources
- Organize and summarize the articles
- Save the daily summary to the `output/` directory

## Configuration

Set the `LLM_PROVIDER` environment variable to choose your preferred provider:
- `openai` - Requires `OPENAI_API_KEY`
- `groq` - Requires `GROQ_API_KEY`
- `ollama` - Default option (local)

## Output

News summaries are saved as timestamped files in the `output/` directory with the format:
`tesla_news_YYYYMMDD_HHMMSS.txt`

## Project Structure

```
TESLA/
├── agents/           # CrewAI agents for news processing
├── config/          # LLM configuration
├── output/          # Generated news summaries
├── tasks/           # CrewAI task definitions
├── tools/           # Additional tools and utilities
├── main.py          # Main application entry point
└── requirements.txt # Python dependencies
```