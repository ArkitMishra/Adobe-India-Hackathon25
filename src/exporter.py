import os
import json

def export_to_json_and_md(linked_json_path, output_json_path, output_md_path):
    """
    Reads linked.json and exports two outputs:
    1. final_output.json → Structured JSON
    2. final_output.md   → Readable Markdown
    """
    # Load linked content
    with open(linked_json_path, 'r', encoding='utf-8') as f:
        linked_data = json.load(f)

    final_output = []
    markdown_lines = []

    markdown_lines.append("# 📘 Structured Document Output\n")

    for item in linked_data:
        heading = item.get("heading", "No Heading Found")
        page = item.get("page", "Unknown Page")
        linked_paragraphs = item.get("linked_paragraphs", [])

        final_output.append({
            "page": page,
            "heading": heading,
            "paragraphs": linked_paragraphs
        })

        markdown_lines.append(f"\n## 📄 Page {page} - {heading}\n")

        for para in linked_paragraphs:
            if isinstance(para, dict):
                text = para.get("text", "").strip()
            else:
                text = str(para).strip()

            if text:
                markdown_lines.append(f"- {text}")

    # Save structured JSON
    with open(output_json_path, 'w', encoding='utf-8') as f_out_json:
        json.dump(final_output, f_out_json, indent=4, ensure_ascii=False)

    # Save Markdown
    with open(output_md_path, 'w', encoding='utf-8') as f_out_md:
        f_out_md.write('\n'.join(markdown_lines))

    print(f"\n✅ Exported final_output.json and final_output.md to {os.path.dirname(output_json_path)}")


# If running directly
if __name__ == "__main__":
    export_to_json_and_md(
        linked_json_path="output/linked.json",
        output_json_path="output/final_output.json",
        output_md_path="output/final_output.md"
    )
