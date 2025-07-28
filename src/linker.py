# src/linker.py

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_semantic_links(document_pages, threshold=0.7):
    """
    Link headings ↔ paragraphs across pages using embedding similarity
    """
    # Flatten all headings and paragraphs with page info
    headings = []
    paragraphs = []

    for page in document_pages:
        page_num = page["page"]
        for h in page["headings"]:
            headings.append({"text": h, "page": page_num})
        for p in page["paragraphs"]:
            paragraphs.append({"text": p, "page": page_num})

    # Embed all texts
    heading_texts = [h["text"] for h in headings]
    para_texts = [p["text"] for p in paragraphs]

    heading_embeddings = model.encode(heading_texts, convert_to_tensor=True)
    para_embeddings = model.encode(para_texts, convert_to_tensor=True)

    # Compare each heading with all paragraphs
    links = []
    for i, h_embed in enumerate(heading_embeddings):
        similarities = util.pytorch_cos_sim(h_embed, para_embeddings)[0]

        for j, score in enumerate(similarities):
            if score >= threshold:
                links.append({
                    "heading": headings[i]["text"],
                    "heading_page": headings[i]["page"],
                    "paragraph": paragraphs[j]["text"],
                    "paragraph_page": paragraphs[j]["page"],
                    "score": round(float(score), 3)
                })

    return links
