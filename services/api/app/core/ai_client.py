import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def explain_code_with_ai(code: str, language: str, user_prompt: str | None = None) -> dict:
    prompt = f"""
You are Axiom, an AI Developer Assistant.

Explain the following {language} code clearly and professionally.

User prompt:
{user_prompt or "No additional prompt provided."}

Code:
{code}

Return the answer in this exact structure:
Summary:
Explanation:
Important Logic:
Possible Issues:
Suggested Improvements:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a precise AI coding assistant for developers."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    output = response.choices[0].message.content or ""

    return {
        "summary": output,
        "explanation": output,
        "important_logic": "Parsed AI response formatting will be improved later.",
        "possible_issues": "Parsed AI response formatting will be improved later.",
        "suggested_improvements": "Parsed AI response formatting will be improved later."
    }
