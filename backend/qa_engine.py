from utils.groq_client import call_groq
from backend.embedding import search_index
import json
import re

# -------- ANSWER --------
def answer_question_with_memory(doc_text, user_question, chat_history, chunks, index):

    if index is None or not chunks:
        return {
            "answer": "No valid document loaded.",
            "justification": ""
        }

    relevant_chunks = search_index(index, user_question, chunks)
    context = "\n".join(relevant_chunks)

    prompt = f"""
Answer ONLY using this context:

{context}

Question: {user_question}
"""

    answer = call_groq(prompt)

    return {
        "answer": answer,
        "justification": context,
        "memory": chat_history
    }


# -------- QUESTIONS --------
def generate_questions(doc_text, chunks, index):

    if not chunks:
        return []

    context = "\n".join(chunks[:3])

    prompt = f"""
Return ONLY valid JSON.

Generate exactly 3 questions with answers.

Format:
[
  {{"question": "Q1", "answer": "A1"}},
  {{"question": "Q2", "answer": "A2"}},
  {{"question": "Q3", "answer": "A3"}}
]

Context:
{context}
"""

    response = call_groq(prompt)

    print("RAW RESPONSE:", response)

    try:
        return json.loads(response)
    except:
        matches = re.findall(r'{"question":\s*"(.*?)",\s*"answer":\s*"(.*?)"}', response)
        return [{"question": q, "answer": a} for q, a in matches] if matches else []
    


    