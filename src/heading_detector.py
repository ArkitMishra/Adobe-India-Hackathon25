# src/heading_detector.py

import statistics

def detect_headings_and_paragraphs(parsed_pages):
    result = []
    paragraph_id = 0  # Global unique ID counter

    for page in parsed_pages:
        blocks = page["content"]
        page_number = page["page"]

        # Collect all heights for analysis
        heights = [block["height"] for block in blocks if "height" in block]
        avg_height = statistics.mean(heights) if heights else 12.0  # fallback default

        page_result = {
            "page": page_number,
            "headings": [],
            "paragraphs": []
        }

        current_paragraph = []

        for block in blocks:
            text = block.get("text", "").strip()
            height = block.get("height", 0)

            if not text:
                continue

            # Mark as heading if height is significantly larger than average
            if height > avg_height * 1.3:
                if current_paragraph:
                    paragraph_text = " ".join(current_paragraph)
                    page_result["paragraphs"].append({
                        "id": f"p{paragraph_id}",
                        "text": paragraph_text
                    })
                    paragraph_id += 1
                    current_paragraph = []
                page_result["headings"].append(text)
            else:
                current_paragraph.append(text)

        if current_paragraph:
            paragraph_text = " ".join(current_paragraph)
            page_result["paragraphs"].append({
                "id": f"p{paragraph_id}",
                "text": paragraph_text
            })
            paragraph_id += 1

        result.append(page_result)

    return result
