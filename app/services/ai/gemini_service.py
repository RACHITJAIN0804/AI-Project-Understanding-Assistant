from google import genai

from app.core.custom_exceptions import AIServiceError
from app.core.settings import settings

client = genai.Client(api_key=settings.gemini_api_key)


def explain_project(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        if not response.text:
            raise AIServiceError("The AI service returned an empty response.")

        return response.text

    except AIServiceError:
        raise

    except Exception as e:
        raise AIServiceError(f"Failed to generate AI explanation: {e}")