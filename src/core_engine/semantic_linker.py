from sentence_transformers import SentenceTransformer, util
import json
from pathlib import Path
from tqdm import tqdm

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_link(input_path, output_path):
    input_file = Path(input_path)
    if not input_file.exists():
        print(f"[✗] ERROR: Input file '{input_path}' not found. Please run heading extraction first.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    linked_output = []

    for page in tqdm(data, desc="Linking paragraphs to headings"):
        page_num = page["page"]
        headings = page["headings"]
        paragraphs = page["paragraphs"]

        if not headings or not paragraphs:
            continue  # Skip pages with missing info

        heading_embeddings = model.encode(headings, convert_to_tensor=True)

        linked_paragraphs = []
        for para in paragraphs:
            if not isinstance(para, str):
                para = str(para)  # Convert to string if not already

            para = para.strip()
            if not para:
                continue  # Skip empty paragraphs

            try:
                para_embedding = model.encode(para, convert_to_tensor=True)
                scores = util.cos_sim(para_embedding, heading_embeddings)[0]
                best_match_index = scores.argmax().item()
                best_heading = headings[best_match_index]
                similarity_score = scores[best_match_index].item()

                linked_paragraphs.append({
                    "text": para,
                    "linked_heading": best_heading,
                    "similarity": round(similarity_score, 3)
                })
            except Exception as e:
                print(f"[!] Error encoding paragraph: {para[:30]}... — {e}")
                continue

        linked_output.append({
            "page": page_num,
            "linked_paragraphs": linked_paragraphs
        })

    # Write linked JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(linked_output, f, indent=4)

    print(f"[✓] Semantic linking completed. Output saved at: {output_path}")
