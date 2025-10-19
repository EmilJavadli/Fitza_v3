# 📄 FITZA Chatbot — AI Assistant for PDF Documents

**FITZA Chatbot** is a Streamlit-based AI web app that allows users to **upload PDF files**, automatically **extract and parse text**, and then **chat interactively** with the document content using Google's **Gemini LLM** and **Landing AI Document Parsing API**.

---

## 🚀 Features

- 🧠 **AI-Powered Chat:** Ask natural-language questions about your PDF content.
- 📘 **PDF Text Extraction:** Uses Landing AI ADE to extract clean text from complex PDFs.
- ⚡ **Fast LLM Responses:** Powered by Gemini 2.0 Flash for low-latency answers.
- 🧩 **Streamlit UI:** Simple, modern interface that works right in your browser.
- 💬 **Session Memory:** Maintains chat history until you upload a new file.

---

## 🧰 Tech Stack

| Component        | Description |
|------------------|-------------|
| **Frontend**     | [Streamlit](https://streamlit.io) |
| **LLM Engine**   | [Google Gemini API (via `google-generativeai`)](https://ai.google.dev) |
| **PDF Parser**   | [Landing AI ADE API](https://landing.ai) |
| **Language**     | Python 3.10 |
| **Environment**  | Conda + pip |

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/fitza-chatbot.git
cd fitza-chatbot
