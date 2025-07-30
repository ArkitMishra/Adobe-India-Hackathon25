
# Adobe India Hackathon 2025 – Project 1 Submission: Intelligent Document Understanding

This repository contains our implementation for **Project 1 – Connecting the Dots: Intelligent Document Understanding** of the [Adobe India Hackathon Challenge 2025](https://d8it4huxumps7.cloudfront.net/files/6874ef2e50a4a_adobe_india_hackathon_challenge_doc.pdf).

The solution extracts structured data from unstructured PDF documents (e.g., whitepapers, policies, manuals) and creates semantic linkages between their content using NLP, heading detection, embedding generation, and semantic search techniques.

---

## 🔍 Problem Statement Overview

- Parse long PDF documents into meaningful sections.
- Identify headings and associate relevant paragraphs.
- Generate semantic embeddings for each section.
- Build a search engine to semantically retrieve relevant content across the document.

---

## 📁 Project Structure

```
Adobe-India-Hackathon25/
├── input/                           # Folder for input PDF files
├── output/                          # Folder for output JSON and semantic link files
├── run.py                           # Main pipeline script that integrates all modules
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── src/
    ├── parser.py                    # Splits PDF into text segments
    ├── heading_detector.py          # Detects headings using regex/ML logic
    ├── linker.py                    # Builds basic parent-child hierarchy between headings and paragraphs
    ├── semantic_linker/
    │   └── semantic_link.py         # Embeds sections and builds semantic relationships
    ├── api.py                       # FastAPI routes to serve the data
    └── web/                         # Frontend folder (React/HTML)
        ├── index.html
        └── styles.css
```

---

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Adobe-India-Hackathon25
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline
```bash
python run.py
```
- Parses all PDFs in `input/`
- Outputs structured JSON and semantic links in `output/`

### 4. Run the Web Interface
```bash
uvicorn src.api:app --reload
```
- Access via browser: `http://127.0.0.1:8000`
- Supports semantic search and document navigation

---

## 🧠 Tech Stack

- **Python 3.10+**
- PyMuPDF (`fitz`) for PDF parsing
- `re` & Rule-based Heading Detection
- `sentence-transformers` for Semantic Embeddings
- FastAPI for backend server
- Basic HTML/CSS or React for frontend

---

## 📊 Output

Each document is processed into:

- A structured JSON with heading and paragraph mappings
- A semantic link file mapping related sections based on content similarity

Example output:

```json
{
  "Document": "AI_Whitepaper.pdf",
  "Sections": [
    {
      "Heading": "Introduction to AI",
      "Paragraphs": ["Artificial Intelligence (AI) is ..."]
    },
    {
      "Heading": "Applications",
      "Paragraphs": ["AI is used in ..."]
    }
  ],
  "Semantic_Links": [
    ["Introduction to AI", "Applications"],
    ["Applications", "Future Scope"]
  ]
}
```

---

## 🧪 Sample Use Case

Given a user query like _"What are the ethical issues in AI?"_, the system returns linked sections from across the document discussing privacy, bias, and governance.

---

## 👨‍💻 Team

**Arkit Mishra** – Engineering @ JUIT  
Email: mishraarkit06@gmail.com  
LinkedIn: [arkit-mishra](https://www.linkedin.com/in/arkit-mishra-892470278/)

**Manya Sharma** – Engineering @ JUIT  
Email: iammanya2k4@gmail.com  
LinkedIn: [manya13](https://www.linkedin.com/in/manya13/)

---

Feel free to fork, explore, and contribute 🚀
