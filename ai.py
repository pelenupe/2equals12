import openai
import os

from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_response(tag):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Black history expert."},
                {"role": "user", "content": f"Tell me about {tag} in Black history."}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI generation failed: {str(e)}"
