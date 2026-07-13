from google import genai

from app.core.settings import settings

client = genai.Client(api_key=settings.gemini_api_key)


def explain_project(prompt: str):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text