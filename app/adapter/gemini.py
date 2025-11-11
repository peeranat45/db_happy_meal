import os
from google import genai

def connect_gemini():
    key = os.getenv("gemini_key")
    client = genai.Client(
        api_key=key
    )
    return client

def prompt_insert(client,  message: str) -> any:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )

    if response and response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
        first_part = response.candidates[0].content.parts[0]
        if hasattr(first_part, 'text'):
            return first_part.text
    
    return "No text content found in the response as expected."


