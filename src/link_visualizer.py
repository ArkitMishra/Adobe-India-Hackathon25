import json
from pathlib import Path

def visualize_links(linked_json_path, output_html_path):
    input_file = Path(linked_json_path)
    if not input_file.exists():
        print(f"[✗] ERROR: Input file '{linked_json_path}' not found. Please run semantic_linker.py first.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = ["<html><head><title>Semantic Linking Output</title><style>"]
    html.append("body { font-family: Arial, sans-serif; padding: 20px; }")
    html.append(".page { margin-bottom: 40px; border-bottom: 1px solid #ccc; padding-bottom: 20px; }")
    html.append(".heading { font-weight: bold; font-size: 18px; color: #2a2a2a; margin-top: 10px; }")
    html.append(".para { margin: 8px 0; }")
    html.append(".score { font-size: 12px; color: gray; }")
    html.append("</style></head><body>")

    for page in data:
        html.append(f'<div class="page"><h2>Page {page["page"]}</h2>')
        for para in page["linked_paragraphs"]:
            html.append(f'<div class="heading">Linked Heading: {para["linked_heading"]}</div>')
            html.append(f'<div class="para">{para["text"]}</div>')
            html.append(f'<div class="score">Similarity: {para["similarity"]}</div><hr>')
        html.append('</div>')

    html.append("</body></html>")

    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))

    print(f"[✓] HTML visualization saved at: {output_html_path}")
