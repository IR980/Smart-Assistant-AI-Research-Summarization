# 🧠 Smart Research Assistant

An AI-powered document assistant that helps users **summarize, ask questions, and test understanding** from PDF/TXT documents using **RAG (Retrieval-Augmented Generation)** and **LLMs (Groq API)**.

---

## 🚀 Features

* 📂 Upload PDF or TXT documents
* ✍️ Paste custom text input
* 📌 Automatic document summarization
* 💬 ChatGPT-style Q&A interface
* 🧠 Context-aware answers using RAG (FAISS)
* 📝 Challenge Mode (auto-generated questions + evaluation)
* ⚡ Fast inference using Groq LLM
* 🧾 Justification with document snippets

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM API:** Groq (LLaMA models)
* **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)
* **Vector DB:** FAISS
* **Parsing:** PyPDF / Text processing

---

## 🧠 How It Works (Architecture)

1. Document is uploaded or pasted
2. Text is split into chunks
3. Embeddings are generated
4. FAISS index is created
5. User query → semantic search
6. Relevant context → sent to LLM
7. LLM generates accurate answer

---

## 📂 Project Structure

```
Smart_Research_Assistant/
│── app.py
│── requirements.txt
│── .env
│
├── backend/
│   ├── qa_engine.py
│   ├── summarizer.py
│   ├── evaluator.py
│   ├── embedding.py
│
├── utils/
│   ├── parser.py
│   ├── chunker.py
│   ├── groq_client.py
│
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
HF_TOKEN=your_huggingface_token (optional)
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app on:

* Streamlit Cloud
* Render
* Hugging Face Spaces

---

## 📸 Screenshots (Optional)

*Add screenshots here for better presentation*

---

## 💼 Resume Highlights

* Built a **RAG-based AI system** for document understanding
* Integrated **Groq LLM API for high-speed inference**
* Implemented **semantic search using FAISS**
* Designed **interactive ChatGPT-style UI using Streamlit**

---

## 🔥 Future Improvements

* Multi-document support
* Chat history persistence (database)
* User authentication
* Voice input/output
* PDF highlighting

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Groq API
* Hugging Face
* Streamlit

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

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
