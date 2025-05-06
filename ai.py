# ---------------------------------------
# ai.py
# Handles AI-powered responses for topics
# ---------------------------------------

# Import necessary libraries
import openai
import os

# Initialize OpenAI client using API key from environment variable
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ---------------------------------------
# Function: generate_ai_response(tag)
# ---------------------------------------
# Sends a prompt to OpenAI asking for information about a given Black history topic
# Returns: A clean, formatted AI-generated response (string)
def generate_ai_response(tag):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Black history expert."},
                {"role": "user", "content": f"Tell me about {tag} in Black history."}
            ]
        )
        # Return the AI's reply (trimmed)
        return response.choices[0].message.content.strip()
    except Exception as e:
        # If something goes wrong, return an error message
        return f"AI generation failed: {str(e)}"
