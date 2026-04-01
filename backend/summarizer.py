from utils.groq_client import call_groq

def summarize(text):

    # ✅ limit text (important for speed + token limit)
    text = text[:3000]

    prompt = f"""
Summarize the following document in simple and clear points (max 150 words):

{text}
"""

    response = call_groq(prompt)

    return response
