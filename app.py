import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.parser import parse_document
from backend.summarizer import summarize
from backend.evaluator import evaluate_answers
from backend.qa_engine import answer_question_with_memory, generate_questions
from backend.embedding import create_embeddings, create_faiss_index
from utils.chunker import chunk_text

st.set_page_config(
    page_title="Smart Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# -------- STYLE --------
st.markdown("""
<style>
.chat-message {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------- CLEAR CHAT --------
if st.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.session_state.chat_history = []

st.title("🧠 Smart Research Assistant")

tab1, tab2 = st.tabs(["📂 Upload File", "✍️ Paste Text"])

doc_text = None

# -------- FILE UPLOAD --------
with tab1:
    uploaded_file = st.file_uploader("Upload PDF or TXT", type=["pdf", "txt"])
    if uploaded_file:
        doc_text = parse_document(uploaded_file)
        st.session_state['doc_text'] = doc_text
        st.session_state['chat_history'] = []

# -------- TEXT INPUT --------
with tab2:
    pasted_text = st.text_area("Paste your text")
    if pasted_text:
        doc_text = pasted_text
        st.session_state['doc_text'] = doc_text
        st.session_state['chat_history'] = []

# -------- PREVIEW FIX ✅ --------
if "doc_text" in st.session_state:
    preview_text = st.session_state['doc_text'].strip()

    if len(preview_text) > 600:
        preview_text = preview_text[:600] + "..."

    with st.expander("📖 Preview File"):
        st.write(preview_text)


# -------- CACHE RAG --------
@st.cache_resource
def prepare_rag(doc_text):

    chunks = chunk_text(doc_text)

    # ✅ FIX: handle empty text
    if not chunks:
        return [], None

    embeddings = create_embeddings(chunks)
    index = create_faiss_index(embeddings)

    return chunks, index


# -------- MAIN --------
if "doc_text" in st.session_state:
    doc_text = st.session_state['doc_text']

    # RAG setup
    chunks, index = prepare_rag(doc_text)

    # ✅ ADD THIS HERE
    if index is None or not chunks:
        st.error("❌ Document is empty or too small")
        st.stop()

    # -------- SUMMARY FIX ✅ --------
    st.subheader("📌 Auto Summary")
    with st.spinner("Generating summary..."):
        try:
            # limit text (IMPORTANT)
            summary = summarize(doc_text[:3000])

            if not summary or "error" in summary.lower():
                st.error("❌ Failed to generate summary")
            else:
                st.success("✅ Summary generated")
                st.write(summary)

        except Exception as e:
            st.error(f"❌ Summary Error: {e}")

    # -------- MODE --------
    mode = st.radio("Choose Mode", ["Ask Anything", "Challenge Me"], horizontal=True)

    # -------- CHAT MODE --------
    if mode == "Ask Anything":

        if "messages" not in st.session_state:
            st.session_state.messages = []

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Chat input
        user_input = st.chat_input("Ask anything about the document...")

        if user_input:
            # Save user message
            st.session_state.messages.append({"role": "user", "content": user_input})

            with st.chat_message("user"):
                st.markdown(user_input)

            # Generate response
            response = answer_question_with_memory(
                doc_text,
                user_input,
                st.session_state['chat_history'],
                chunks,
                index
            )

            answer = response["answer"]
            context = response["justification"]

            # Show AI response
            with st.chat_message("assistant"):
                st.markdown(answer)

                with st.expander("📄 View Context"):
                    st.write(context)

            # Save response
            st.session_state.messages.append({"role": "assistant", "content": answer})

            # Save memory
            st.session_state.chat_history.append({
                "question": user_input,
                "answer": answer
            })

    # -------- CHALLENGE MODE --------
    else:
        if st.button("Generate Questions"):
            questions = generate_questions(doc_text, chunks, index)

            if not questions:
                st.error("❌ Failed to generate questions")
            else:
                st.session_state['questions'] = questions

        if "questions" in st.session_state:
            for i, q in enumerate(st.session_state['questions']):
                st.write(f"### Q{i+1}: {q['question']}")
                user_ans = st.text_input(f"Your Answer {i+1}", key=i)

                if user_ans:
                    result = evaluate_answers(
                        q["question"], user_ans, q["answer"], doc_text
                    )
                    st.write("✅ Feedback:", result["feedback"])
                    st.write("📌 Justification:", result["justification"])
