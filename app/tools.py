from tavily import TavilyClient
from app.config import TAVILY_API_KEY


client = TavilyClient(api_key=TAVILY_API_KEY)


def search_news(topic):

    response = client.search(
        query=topic,
        search_depth="advanced",
        max_results=5
    )

    results = response.get("results", [])

    combined_text = ""

    for item in results:

        title = item.get("title", "")
        content = item.get("content", "")

        combined_text += f"""
TITLE:
{title}

CONTENT:
{content}

"""

    return combined_text