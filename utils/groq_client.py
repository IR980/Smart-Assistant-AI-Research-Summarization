# import os
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def call_groq(prompt: str) -> str:
#     try:
#         response = client.chat.completions.create(
#             model="llama-3.1-8b-instant",   # Best Groq model
#             messages=[
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         if "Rate limit" in str(e):
#             return "❌ Groq API Rate Limit Exceeded. Please try again later."
        
#         return f"❌ Groq Error: {str(e)}"
    

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # ✅ stable model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        if "rate limit" in str(e).lower():
            return "⚠️ Rate limit reached. Try again later."

        return f"❌ Groq Error: {str(e)}"