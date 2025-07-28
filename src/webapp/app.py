from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from pathlib import Path
from difflib import SequenceMatcher

app = FastAPI()

# Static and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load final_output.json
FINAL_JSON_PATH = Path("../../output/final_output.json")  # Adjusted relative path
data = []

if FINAL_JSON_PATH.exists():
    try:
        with open(FINAL_JSON_PATH, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # Extract heading + paragraph text
        for entry in raw_data:
            heading = entry.get("heading", "No Heading")
            for para in entry.get("paragraphs", []):
                para_text_raw = para.get("text", "")
                try:
                    # Convert stringified dict to real dict
                    para_dict = eval(para_text_raw) if isinstance(para_text_raw, str) else para_text_raw
                    para_text = para_dict.get("text", "")
                except Exception:
                    para_text = para_text_raw  # fallback if eval fails
                data.append({
                    "heading": heading,
                    "content": para_text
                })

    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format in final_output.json")
else:
    print("[WARNING] final_output.json not found. App will run with empty data.")

# Semantic search
def semantic_search(query, entries, threshold=0.4):
    matches = []
    for item in entries:
        heading = item.get("heading", "")
        content = item.get("content", "")
        combined = f"{heading} {content}"
        score = SequenceMatcher(None, query.lower(), combined.lower()).ratio()
        if score >= threshold:
            matches.append({**item, "score": round(score, 2)})
    return sorted(matches, key=lambda x: x["score"], reverse=True)

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": data})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = ""):
    results = semantic_search(q, data)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": q})

@app.get("/api/data")
async def get_json():
    return JSONResponse(content={"status": "success", "data": data if data else []})
