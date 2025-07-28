from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json
from difflib import SequenceMatcher

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
OUTPUT_FILE = BASE_DIR.parent.parent / "output" / "final_output.json"

# Mount assets
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Parse data from final_output.json
parsed_data = []
if OUTPUT_FILE.exists():
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        for page in raw_data:
            for para in page.get("linked_paragraphs", []):
                heading = para.get("linked_heading", "No Heading")
                text = para.get("text", "")
                score = para.get("similarity", None)
                parsed_data.append({
                    "heading": heading,
                    "content": text,
                    "score": round(score, 2) if score else None
                })
else:
    print(f"[WARNING] {OUTPUT_FILE} not found. Starting with empty data.")

# Basic semantic match using difflib
def semantic_search(query, data, threshold=0.4):
    matches = []
    for item in data:
        combined = f"{item['heading']} {item['content']}"
        score = SequenceMatcher(None, query.lower(), combined.lower()).ratio()
        if score >= threshold:
            matches.append({**item, "score": round(score, 2)})
    return sorted(matches, key=lambda x: x["score"], reverse=True)

# Routes
@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": parsed_data})

@app.get("/search", response_class=HTMLResponse)
def search(request: Request, q: str = ""):
    results = semantic_search(q, parsed_data)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": q})
