<<<<<<< HEAD
# 🧠 Smart Research Assistant

An AI-powered research assistant that allows users to **upload documents or paste text**, generate **summaries**, ask **context-aware questions**, and test their understanding through **interactive challenges**.

Built using **Streamlit + Groq LLM + RAG (Retrieval-Augmented Generation)**.
=======

# 🧠 Smart Assistant for Research Summarization

A GenAI-powered assistant that reads uploaded documents and helps users:
- Answer complex, logic-based questions
- Summarize research material
- Evaluate user comprehension
- Justify all answers with references from source
- A powerful, interactive assistant that helps you summarize, query, and test
- your understanding of research documents (PDF/TXT)
- using advanced language models and semantic search.
-  Built with Streamlit for an intuitive dashboard experience.
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d

---

## 🚀 Features

<<<<<<< HEAD
* 📂 Upload PDF/TXT files or paste text
* 📌 Auto-generate concise summaries
* 💬 ChatGPT-style Q&A interface
* 🧠 Context-aware answers using RAG (FAISS + embeddings)
* 📝 Challenge mode with auto-generated questions
* ✅ Answer evaluation with feedback & justification
* ⚡ Fast inference using Groq API
=======
https://smartassistantirshad.streamlit.app/
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d

---

## 🏗️ Tech Stack

<<<<<<< HEAD
* **Frontend/UI**: Streamlit
* **LLM**: Groq (LLaMA 3.1)
* **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
* **Vector Search**: FAISS
* **Backend**: Python
=======
---
<img width="1902" height="1022" alt="smart-1" src="https://github.com/user-attachments/assets/f57dc272-36b3-4935-9ca4-0525050d8c40" />


---

<img width="1912" height="1030" alt="smart-2" src="https://github.com/user-attachments/assets/ecf6fd9c-4e9c-43af-bdc5-687309cce1b3" />

---
<img width="1907" height="1022" alt="smart-3" src="https://github.com/user-attachments/assets/e2c5ef92-d086-4246-809b-f6bf14cb97a7" />

---

📹 Loom: https://www.loom.com/share/31957017e6bb4e25acc374133c3927db

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/IR980/smart-assistant-research-summarization.git
cd smart-assistant-research-summarization

```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
venv/Scripts/activate
      
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run src/app.py
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d

```
### 4. Set up API Key
# Create a .env file:
```
OPENAI_API_KEY=your_openai_key_here

```
---

## 📂 Project Structure

```
<<<<<<< HEAD
Smart_Research_Assistant/
│
├── app.py                  # Main Streamlit app
├── requirements.txt       # Dependencies
│
├── backend/
│   ├── qa_engine.py       # Q&A + question generation
│   ├── summarizer.py      # Summary generation
│   ├── evaluator.py       # Answer evaluation
│   ├── embedding.py       # Embeddings + FAISS search
│
├── utils/
│   ├── parser.py          # PDF/TXT parsing
│   ├── chunker.py         # Text chunking
│   ├── groq_client.py     # Groq API integration
=======
src/
│
├── app.py                        # Main Streamlit app
├── challenge/
│   └── question_generator.py     # Challenge mode logic
├── embedding/
│   ├── embedder.py               # Embedding functions
│   └── vector_store.py           # Vector search
├── utils/
│   └── helpers.py                # Utilities (chunking, highlighting, etc.)
├── document_processing/
│   ├── pdf_parser.py             # PDF text extraction
│   └── text_extractor.py         # TXT extraction
├── qa/
│   ├── question_answering.py     # LLM Q&A logic
│   └── openai_client.py          # OpenAI client
└── evaluator/
    └── answer_evaluator.py       # Answer evaluation logic

>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

<<<<<<< HEAD
```bash
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant
```
=======

 - **main.py** – User interface (Streamlit) and backend interaction
 - **logic.py** - Core logic and LLM/document processing
 - **utils.py** - Helper and utility functions

### Flow:

1. Launches the Streamlit app.
2. Manages file upload, mode selection, and user inputs.
3. Calls functions from logic.py and displays results.
4. Handles text extraction from PDF/TXT.
5. Splits text into chunks and generates embeddings.
6. Performs semantic search and context retrieval.
7. Interfaces with the LLM for Q&A, summarization, and challenge generation
8. Text chunking and formatting utilities.
9. Prompt construction helpers.
10. Answer evaluation and scoring functions.
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d

---

### 2️⃣ Create virtual environment

<<<<<<< HEAD
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```
=======
- Python 3.10+
- Streamlit
- sentence-transformers
- PyMuPDF (pip install pymupdf)
- penAI Python SDK
- See requirements.txt for full list
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d

---

### 3️⃣ Install dependencies

<<<<<<< HEAD
```bash
pip install -r requirements.txt
```
=======


📹 Loom: [https://www.loom.com/share/your-demo-link](https://www.loom.com/share/31957017e6bb4e25acc374133c3927db)
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d

---

## 🔐 Environment Setup

<<<<<<< HEAD
Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

Deployed easily using **Streamlit Cloud**:

1. Push project to GitHub
2. Go to https://share.streamlit.io
3. Connect repo & deploy
4. Add API key in **Secrets**

---

## 🧠 How It Works (RAG Pipeline)

1. 📄 Input document (PDF/TXT)
2. ✂️ Split into chunks
3. 🔢 Convert into embeddings
4. 📦 Store in FAISS index
5. 🔍 Retrieve relevant chunks
6. 🤖 Generate answer using Groq LLM

---

## 🎯 Use Cases

* 📚 Study assistant for students
* 📄 Document analysis & summarization
* 🧠 Interview preparation
* 🏢 Knowledge base assistant

---

## 📸 Screenshots (Optional)

*Add screenshots of your app UI here*

---

## 🚀 Future Improvements

* 📂 Multi-document support
* 💾 Persistent vector database
* 🔐 User authentication
* 🎨 Advanced UI/UX improvements
* 🌍 Multi-language support

---

## 👨‍💻 Author

**Irshad Alam**

---

## ⭐ Support

If you like this project, please ⭐ the repo and share it!

---
=======
**Irshad Alam**  
[GitHub](https://github.com/IR980)


Built with ❤️ using Gemini + Streamlit By Irshad
>>>>>>> cafcb17a39745d44e3ab727bf636f45de220065d
