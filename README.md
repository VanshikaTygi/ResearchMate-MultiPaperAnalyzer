# 📚 ResearchMate AI
### Multi-Agent Research Intelligence Platform

ResearchMate AI is an intelligent multi-agent research assistant designed to simplify the process of understanding and analyzing research papers.

Instead of manually reading multiple research papers, users can upload one or more PDFs and interact with them using AI-powered agents capable of generating structured summaries, answering research questions, comparing multiple papers, and identifying potential research gaps.

The project combines Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Semantic Search, and a Multi-Agent Architecture to create an interactive research intelligence platform.

---

# 🚀 Features

✅ Upload one or multiple research papers (PDF)

✅ Automatic PDF text extraction

✅ Intelligent text chunking

✅ Semantic search using FAISS Vector Database

✅ AI-generated structured research summaries

✅ Research Question & Answering

✅ Multi-paper comparison

✅ Research gap discovery

✅ Multi-Agent architecture

✅ Interactive Streamlit interface

✅ Modular project structure

---

# 🏗 Project Architecture

```
                    User

                      │
                      ▼

          Upload Research Papers (PDF)

                      │
                      ▼

             PDF Text Extraction

                      │
                      ▼

              Text Chunking

                      │
                      ▼

         Sentence Embedding Generation

                      │
                      ▼

             FAISS Vector Database

                      │
                      ▼

              Coordinator Agent
                      │
     ┌────────┬────────┬────────┬────────┐
     ▼        ▼        ▼        ▼
 Analysis   Q&A    Comparison Innovation
  Agent    Agent      Agent      Agent

     └────────┴────────┴────────┴────────┘
                      │
                      ▼

             Streamlit User Interface
```

---

# 🤖 AI Agents

## 🎯 Coordinator Agent

Acts as the central controller of the application.

Responsibilities:

- Understand user request
- Route task to appropriate AI agent
- Coordinate workflow
- Return final response

---

## 📄 Analysis Agent

Responsible for generating structured summaries of uploaded research papers.

Capabilities:

- Paper Summary
- Objectives
- Methodology
- Results
- Key Contributions
- Limitations

---

## ❓ Research Q&A Agent

Allows users to ask natural language questions related to uploaded research papers.

Capabilities:

- Context-aware answers
- Semantic search
- Research-specific responses
- Grounded AI outputs

---

## 📊 Comparison Agent

Compares multiple uploaded research papers.

Capabilities:

- Methodology comparison
- Dataset comparison
- Strengths
- Weaknesses
- Advantages
- Limitations

---

## 💡 Innovation Agent

Identifies possible future research opportunities.

Capabilities:

- Research Gap Discovery
- Future Scope
- Innovation Suggestions
- Improvement Ideas

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Streamlit | User Interface |
| LangChain | AI Workflow |
| FAISS | Vector Database |
| Sentence Transformers | Text Embeddings |
| Groq API | Large Language Model |
| PyMuPDF | PDF Processing |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 📂 Project Structure

```
ResearchMate-MultiPaperAnalyzer/

│

├── agents/
│   ├── coordinator_agent.py
│   ├── analysis_agent.py
│   ├── comparison_agent.py
│   ├── innovation_agent.py
│
├── services/
│   ├── pdf_processor.py
│   ├── vector_store.py
│
├── ui/
│   ├── sidebar_ui.py
│   ├── main_ui.py
│   ├── coordinator_ui.py
│   ├── expert_ui.py
│
├── app.py
├── requirements.txt
├── prompt.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/<VanshikaTygi>/ResearchMate-MultiPaperAnalyzer.git
```

---

## Move into Project

```bash
cd ResearchMate-MultiPaperAnalyzer
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_API_KEY
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 🖥 Application Workflow

1. Upload one or more research papers.

2. Extract text from uploaded PDFs.

3. Split text into meaningful chunks.

4. Generate semantic embeddings.

5. Store embeddings in FAISS.

6. Coordinator Agent receives the request.

7. Appropriate AI Agent processes the task.

8. Response is displayed on the Streamlit interface.

---


# 🎯 Project Objectives

The objective of ResearchMate AI is to reduce the effort involved in manually studying research papers by providing AI-assisted analysis and interaction.

The system aims to:

- Improve literature review efficiency

- Enable semantic search over research papers

- Provide AI-powered research assistance

- Compare multiple papers automatically

- Discover research gaps

- Suggest future research directions

---

# 🌟 Future Enhancements

- Citation-based responses

- Automatic report generation

- PDF export

- Research paper recommendation system

- Interactive knowledge graphs

- Multi-language support

- Research timeline visualization

- Additional specialized AI agents

- Cloud deployment improvements

---

# 👩‍💻 Author

**Vanshika Tyagi**

B.Tech Computer Science and Engineering (AI & ML)

Lovely Professional University

---

# 🙏 Acknowledgements

This project was developed as part of the **AI Engineering Launchpad – LLM & Agentic AI** Summer Training Program.

Special thanks to the faculty members and mentors for their guidance throughout the project development process.

---

# 📄 License

This project is developed for educational and learning purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.