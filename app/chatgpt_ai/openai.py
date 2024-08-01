from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv('CHATGPT_API_KEY')

def chatgpt_response(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-4o-mini",  
            prompt=prompt,
            temperature=1,
            max_tokens=100
        )

        response_dict = response.get("choices")
        if response_dict and len(response_dict) > 0:
            prompt_response = response_dict[0]["text"]
        return prompt_response
    
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"
