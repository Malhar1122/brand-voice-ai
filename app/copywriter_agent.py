import time

from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import (
    GOOGLE_API_KEY,
    MODEL_NAME,
    MAX_RETRIES
)

from app.voice_profiles import VOICE_PROFILES
from app.logger import logger


llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7
)


def generate_posts(summary, voice):

    logger.info(f"Generating posts using voice: {voice}")

    voice_style = VOICE_PROFILES.get(
        voice,
        VOICE_PROFILES["corporate"]
    )

    prompt = f"""
You are an elite AI copywriter.

Generate:

1. LinkedIn post
2. X/Twitter post

NEWS SUMMARY:
{summary}

BRAND VOICE:
{voice_style}

IMPORTANT FACTUAL RULES:
- Only use information present in the provided summary.
- Do not invent facts or future claims.
- Avoid assumptions not supported by the news summary.
- Stay factually grounded.

RETURN FORMAT:

LINKEDIN POST:
<linkedin post>

TWITTER POST:
<twitter post>

RULES:

LINKEDIN:
- professional formatting
- engaging hook
- insightful commentary
- ending CTA
- platform appropriate
- around 120-200 words
- use shorter paragraphs
- adapt strongly to selected voice

TWITTER/X:
- concise
- punchy
- high engagement
- platform optimized
- maximum 220 characters preferred
- avoid unnecessary filler
- adapt strongly to selected voice

IMPORTANT:
LinkedIn and Twitter tone must clearly reflect
the selected brand voice.
"""

    for attempt in range(MAX_RETRIES):

        try:

            response = llm.invoke(prompt)

            logger.info("Posts generated successfully.")

            return response.content

        except Exception as e:

            logger.error(
                f"Copywriter Agent Error Attempt {attempt+1}: {str(e)}"
            )

            time.sleep(3)

    return """
LINKEDIN POST:
Failed to generate LinkedIn post.

TWITTER POST:
Failed to generate Twitter post.
"""