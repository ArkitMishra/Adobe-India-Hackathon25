# src/final_assembler.py

import json
from collections import defaultdict

def assemble_sections(structured_data, semantic_links):
    """
    Reassemble the document by grouping semantically linked paragraphs.
    """
    # Map paragraph_id to content for quick lookup
    para_map = {para['id']: para for para in structured_data}

    # Group paragraphs based on link clusters
    grouped_sections = defaultdict(list)
    visited = set()
    section_id = 1

    for link in semantic_links:
        src = link['source']
        tgt = link['target']

        if src not in visited or tgt not in visited:
            # Create a new section group if not already visited
            group_key = f"Section_{section_id}"
            grouped_sections[group_key].append(para_map[src])
            grouped_sections[group_key].append(para_map[tgt])
            visited.update([src, tgt])
            section_id += 1

    # Add any remaining unlinked paragraphs as separate sections
    for para_id, para in para_map.items():
        if para_id not in visited:
            group_key = f"Section_{section_id}"
            grouped_sections[group_key].append(para)
            section_id += 1

    # Convert to list format for JSON output
    final_output = []
    for section, paras in grouped_sections.items():
        final_output.append({
            "section_id": section,
            "content": paras
        })

    return final_output

def save_final_output(output_data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
