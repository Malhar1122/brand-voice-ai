import time

from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    MAX_RETRIES
)

from app.tools import search_news
from app.logger import logger


llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)


def research_topic(topic):

    logger.info(f"Researching topic: {topic}")

    try:

        raw_news = search_news(topic)

    except Exception as e:

        logger.error(f"Tavily Error: {str(e)}")

        return "Unable to fetch live news."

    prompt = f"""
You are an expert news analyst.

Analyze and summarize the latest news.

TOPIC:
{topic}

LIVE NEWS:
{raw_news}

RETURN:
- key trends
- concise summary
- major insights
- future implications

Keep response professional and concise.
"""

    for attempt in range(MAX_RETRIES):

        try:

            response = llm.invoke(prompt)

            logger.info("Research summary generated.")

            return response.content

        except Exception as e:

            logger.error(
                f"Research Agent Error Attempt {attempt+1}: {str(e)}"
            )

            time.sleep(3)

    return "Research generation failed after retries."