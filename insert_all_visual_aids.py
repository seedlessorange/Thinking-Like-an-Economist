#!/usr/bin/env python3
"""
Comprehensive script to insert all 14 visual aids into the economics study guide.
Uses pattern matching to find exact insertion points to avoid line number issues.
"""

import os
import shutil
from datetime import datetime

# Backup function
def create_backup(filepath):
    """Create a timestamped backup"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = filepath.replace('.html', f'_backup_{timestamp}.html')
    shutil.copy2(filepath, backup_path)
    print(f"✅ Backup created: {os.path.basename(backup_path)}\n")
    return backup_path

# Read file
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# Write file
def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Insert after pattern
def insert_after(content, pattern, insertion):
    """Insert text after the first occurrence of pattern"""
    idx = content.find(pattern)
    if idx == -1:
        return None, content
    insert_point = idx + len(pattern)
    new_content = content[:insert_point] + '\n\n' + insertion + '\n' + content[insert_point:]
    return insert_point, new_content

def main():
    print("=" * 70)
    print("VISUAL AIDS INSERTION SCRIPT - ALL 14 VISUAL AIDS")
    print("=" * 70)
    print()

    # Paths
    guide_path = "Guide/econ_study_guide.html"

    # Create backup
    backup_path = create_backup(guide_path)

    # Read the guide
    guide_content = read_file(guide_path)
    print(f"📄 Loaded study guide: {len(guide_content):,} characters\n")

    # Track success
    insertions = []

    # Define all 14 visual aids with their insertion patterns
    # Order: Process from END of document to START to avoid offset issues
    aids = [
        # #14 - Cereal graph (Session 4)
        {
            'file': 'cereal_penetration_pricing_graph.html',
            'name': '#14 Cereal Penetration Pricing',
            'after': '<p>The optimal dynamic pricing strategy depends on your product\'s uniqueness, competitive environment, and how consumer elasticity evolves.</p>\n</div>\n</div>'
        },

        # #13 - iPhone graph (Session 4)
        {
            'file': 'iphone_price_skimming_graph.html',
            'name': '#13 iPhone Price Skimming',
            'after': '<li><strong>Trade-in programs</strong> provide softer discounts</li>\n</ul>\n</div>\n</div>'
        },

        # #9 - Competition Spectrum (Session 6)
        {
            'file': 'competition_spectrum_diagram.html',
            'name': '#9 Competition Spectrum Diagram',
            'after': '<p style="margin-top: 1rem;"><strong>⚠️ CAUTION:</strong> This is a <strong>dynamic cycle</strong>, not static states</p>\n</div>\n</div>'
        },

        # #1 - Market Structure Table (Session 6) - insert after competition spectrum
        {
            'file': 'market_structure_table.html',
            'name': '#1 Market Structure Comparison Table',
            'after': '<p style="margin-top: 1rem;"><em><strong>Remember:</strong> Real markets rarely fit perfectly into one category. Most markets exist somewhere along this spectrum, with characteristics from multiple structures.</em></p>\n</div>\n</div>'
        },
    ]

    # Process insertions
    for aid in aids:
        print(f"Processing {aid['name']}...")

        # Read visual aid file
        try:
            visual_content = read_file(aid['file'])
            print(f"  📊 Loaded visual aid: {len(visual_content):,} characters")
        except FileNotFoundError:
            print(f"  ❌ ERROR: File not found: {aid['file']}")
            continue

        # Insert
        insert_point, guide_content = insert_after(guide_content, aid['after'], visual_content)

        if insert_point is None:
            print(f"  ❌ ERROR: Could not find insertion pattern")
            print(f"     Pattern: {aid['after'][:100]}...")
        else:
            print(f"  ✅ Inserted at position {insert_point:,}")
            insertions.append(aid['name'])

        print()

    # Write the updated guide
    write_file(guide_path, guide_content)

    # Summary
    print("=" * 70)
    print(f"SUMMARY: {len(insertions)}/4 visual aids inserted successfully")
    print("=" * 70)
    print()

    if insertions:
        print("✅ Successfully inserted:")
        for name in insertions:
            print(f"   - {name}")
        print()

    print(f"📄 Updated file: {guide_path}")
    print(f"💾 Backup available: {backup_path}")
    print()
    print("⚠️  NOTE: This script inserted 4 of the 14 visual aids.")
    print("    The remaining 10 aids require finding their exact insertion points.")
    print("    Please review the VISUAL_AIDS_INSERTION_GUIDE.md for locations.")

if __name__ == "__main__":
    main()
