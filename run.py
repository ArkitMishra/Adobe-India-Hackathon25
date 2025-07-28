# run.py

from src import parser, heading_detector, linker
from src.core_engine.semantic_linker import semantic_link
from src import exporter
from datetime import datetime
import json
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.endswith(".pdf"):
            filepath = os.path.join(INPUT_FOLDER, filename)
            print(f"\n📄 Parsing File: {filename}")

            # Step 1: Extract raw text per page
            parsed_pages = parser.extract_text_from_pdf(filepath)

            # Step 2: Detect headings and group paragraphs
            print("🔍 Detecting Headings and Paragraphs...")
            structured_data = heading_detector.detect_headings_and_paragraphs(parsed_pages)

            # Step 3: Save intermediate structured data
            heading_json_path = os.path.join(OUTPUT_FOLDER, "headings_and_paragraphs.json")
            with open(heading_json_path, "w", encoding="utf-8") as f:
                json.dump(structured_data, f, indent=4, ensure_ascii=False)

            # Step 4: Semantic Linking (Headings ↔ Paragraphs)
            print("🔗 Linking Related Content Semantically...")
            linked_json_path = os.path.join(OUTPUT_FOLDER, "linked.json")
            semantic_link(heading_json_path, linked_json_path)

            # Step 5: Load semantic links (optional visualization or cross-check)
            links = linker.get_semantic_links(structured_data)

            # Step 6: Save intermediate files
            base_filename = filename.replace(".pdf", "")
            output_base_path = os.path.join(OUTPUT_FOLDER, base_filename)

            with open(f"{output_base_path}_structured.json", "w", encoding="utf-8") as f:
                json.dump(structured_data, f, indent=4, ensure_ascii=False)

            with open(f"{output_base_path}_links.json", "w", encoding="utf-8") as f:
                json.dump(links, f, indent=4, ensure_ascii=False)

            # Step 7: Export final_output.json and final_output.md
            print("📤 Exporting Final Output in JSON and Markdown formats...")
            output_json_path = os.path.join(OUTPUT_FOLDER, "final_output.json")
            output_md_path = os.path.join(OUTPUT_FOLDER, "final_output.md")

            exporter.export_to_json_and_md(
                linked_json_path=linked_json_path,
                output_json_path=output_json_path,
                output_md_path=output_md_path
            )

            print(f"✅ All output saved to /output for {filename}")

if __name__ == "__main__":
    main()
