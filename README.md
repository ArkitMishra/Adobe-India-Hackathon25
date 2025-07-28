
# Adobe India Hackathon 2025 – Project 1 Submission

This repository contains my implementation for **Project 1** of the [Adobe India Hackathon Challenge](https://d8it4huxumps7.cloudfront.net/files/6874ef2e50a4a_adobe_india_hackathon_challenge_doc.pdf). The solution extracts and analyzes information from multiple resume PDFs using various NLP and image processing techniques.

## 🔍 Project Description

The goal of this project is to automatically analyze a batch of resumes (PDFs) and extract key details like:

- Name
- Email
- Phone Number
- Education
- Skills
- Work Experience

The output is stored in a structured JSON format for each resume, enabling easy downstream processing and decision-making.

## 📁 Directory Structure

Adobe-India-Hackathon25/
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py                  # Main pipeline for PDF parsing and data extraction
├── input/                  # Folder for input PDFs
├── output/                 # Folder where output JSONs are saved
├── src/
│   ├── parser.py           # Custom extraction and NLP logic
│   ├── utils.py            # Helper functions
│   └── webapp/             # FastAPI webapp folder
│       └── app.py          # Web server to serve parsed data

## 🚀 Installation and Setup

1. **Clone the Repository**
   git clone <your-repo-url>
   cd Adobe-India-Hackathon25

2. **Install Required Python Libraries**
   pip install pdfplumber pytesseract pillow opencv-python PyMuPDF sentence-transformers fastapi uvicorn

3. **(Optional but Recommended) Use Virtual Environment**
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

4. **Run the Resume Parser**
   python run.py

   This will:
   - Read all PDF files from the `input/` directory.
   - Extract structured data (name, email, skills, etc.).
   - Store the results as JSON files in the `output/` directory.

5. **Start the Web Application**
   cd src/webapp
   uvicorn app:app --reload
   (If the above doesn't work, use: python -m uvicorn app:app --reload)

   This runs a FastAPI server where you can interact with the results via browser or API calls.

## 🧠 Tech Stack

- Python
- pdfplumber
- PyMuPDF
- pytesseract (OCR)
- OpenCV
- Pillow
- sentence-transformers (NLP)
- FastAPI + Uvicorn (Web App)

## 📦 Output

Each resume is processed and a structured JSON file is created under the `output/` directory. These contain extracted fields like:

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+91-XXXXXXXXXX",
  "skills": ["Python", "Machine Learning", "NLP"],
  "education": ["B.Tech CSE - JUIT"],
  "experience": "2 years at XYZ Corp"
}

## 📌 Notes

- Make sure Tesseract OCR is installed on your system and properly configured (if OCR is required).
- Ensure that the input PDFs are stored in the `input/` folder before running the script.
- Tested on Python 3.10.

## 👨‍💻 Author

Arkit – Engineering @ JUIT  
Contact: [Your email or LinkedIn if applicable]

---

Feel free to fork and use for learning or enhancements!
