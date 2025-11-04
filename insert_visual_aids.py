#!/usr/bin/env python3
"""
Script to insert all 14 visual aids into the economics study guide.
Inserts are done in reverse order (highest line number first) to avoid offset issues.
"""

import re

# Define visual aids with their insertion markers and files
VISUAL_AIDS = [
    # Format: (search_pattern, insert_after_pattern, visual_aid_file, description)

    # Session 4 - Cereal case study
    ("</div>\n\n\n<h3>Case Study: New Cereal Brand", "cereal_penetration_pricing_graph.html", "Cereal Penetration Pricing"),

    # Session 4 - iPhone case study
    ("</div>\n</div>\n\n<div class=\"content-card\">\n<h4 style=\"color: #3498db;\"><i class=\"fas fa-users\"></i> Strategy 2:", "iphone_price_skimming_graph.html", "iPhone Price Skimming"),

    # Session 6/7 - Competition spectrum section
    ("<p style=\"margin-top: 1rem;\"><strong>⚠️ CAUTION:</strong> This is a <strong>dynamic cycle</strong>, not static states</p>\n</div>\n</div>", "competition_spectrum_diagram.html", "Competition Spectrum"),

    # After competition spectrum
    ("<p style=\"margin-top: 1rem;\"><strong>⚠️ CAUTION:</strong> This is a <strong>dynamic cycle</strong>, not static states</p>\n</div>\n</div>", "market_structure_table.html", "Market Structure Table"),
]

def find_insertion_point(lines, pattern):
    """Find the line index where pattern ends"""
    pattern_lines = pattern.split('\n')
    for i in range(len(lines) - len(pattern_lines) + 1):
        if all(lines[i + j].rstrip() == pattern_lines[j].rstrip()
               for j in range(len(pattern_lines))):
            return i + len(pattern_lines)
    return None

def insert_visual_aid(guide_path, visual_aid_file, search_pattern, description):
    """Insert a visual aid file after the search pattern"""
    print(f"Inserting {description}...")

    # Read the guide
    with open(guide_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Read the visual aid
    with open(visual_aid_file, 'r', encoding='utf-8') as f:
        visual_content = f.read()

    # Find insertion point
    insert_idx = find_insertion_point(lines, search_pattern)

    if insert_idx is None:
        print(f"  ❌ Could not find insertion point for {description}")
        return False

    # Insert the visual aid
    lines.insert(insert_idx, '\n' + visual_content + '\n')

    # Write back
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"  ✅ Inserted at line {insert_idx}")
    return True

def main():
    guide_path = "Guide/econ_study_guide.html"

    print("=" * 60)
    print("VISUAL AIDS INSERTION SCRIPT")
    print("=" * 60)
    print()

    success_count = 0

    # Process in order
    for search_pattern, visual_file, description in VISUAL_AIDS:
        if insert_visual_aid(guide_path, visual_file, search_pattern, description):
            success_count += 1
        print()

    print("=" * 60)
    print(f"SUMMARY: {success_count}/{len(VISUAL_AIDS)} visual aids inserted successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()
