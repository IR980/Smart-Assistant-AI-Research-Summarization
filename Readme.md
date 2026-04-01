# 🧠 Smart Research Assistant

An AI-powered research assistant that allows users to **upload documents or paste text**, generate **summaries**, ask **context-aware questions**, and test their understanding through **interactive challenges**.

Built using **Streamlit + Groq LLM + RAG (Retrieval-Augmented Generation)**.

---

## 🚀 Features

* 📂 Upload PDF/TXT files or paste text
* 📌 Auto-generate concise summaries
* 💬 ChatGPT-style Q&A interface
* 🧠 Context-aware answers using RAG (FAISS + embeddings)
* 📝 Challenge mode with auto-generated questions
* ✅ Answer evaluation with feedback & justification
* ⚡ Fast inference using Groq API

---

## 🏗️ Tech Stack

* **Frontend/UI**: Streamlit
* **LLM**: Groq (LLaMA 3.1)
* **Embeddings**: Sentence Transformers (`all-MiniLM-L6-v2`)
* **Vector Search**: FAISS
* **Backend**: Python

---

## 📂 Project Structure

```
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
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

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
