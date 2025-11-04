#!/usr/bin/env python3
"""Final comprehensive script to insert all remaining 11 visual aids"""

import shutil
from datetime import datetime

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_after(content, after_pattern, insertion_content):
    """Insert content after pattern, return new content and success boolean"""
    idx = content.find(after_pattern)
    if idx == -1:
        return content, False
    insert_point = idx + len(after_pattern)
    new_content = content[:insert_point] + '\n\n' + insertion_content + '\n' + content[insert_point:]
    return new_content, True

def main():
    print("=" * 70)
    print("FINAL VISUAL AIDS INSERTION - Remaining 11 Aids")
    print("=" * 70)
    print()

    # Backup
    guide_path = 'Guide/econ_study_guide.html'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup = f'Guide/econ_study_guide_backup2_{timestamp}.html'
    shutil.copy2(guide_path, backup)
    print(f"✅ Backup: {backup}\n")

    content = read_file(guide_path)
    inserted = []

    # Remaining 11 visual aids - insert from END to START of document
    aids = [
        # Use grep to find exact patterns then insert
        ('market_structure_table.html', '#1 Market Structure Table', '</div>\n</div>\n\n<div class="content-card">\n<h3 style="display: flex; align-items: center; margin-top: 0;">\n<div class="section-icon"><i class="fas fa-chess"></i></div>\n<span>Part 1: Highly Competitive Markets'),
        ('lrac_curve.html', '#2 LRAC Curve', 'minimize costs in both short-run and long-run!</strong></p>\n</div>'),
        ('elasticity_comparison.html', '#3 Elasticity Comparison', '<div class="content-card">\n<h3 style="margin-top: 0;"><i class="fas fa-chart-line"></i> Worked Example: Calculating and Interpreting Elasticity</h3>'),
        ('elasticity_reference_table.html', '#6 Elasticity Reference Table', '<li><strong>Price elasticity of supply (PES)</strong> = How responsive quantity supplied is to price changes</li>\n</ul>\n</div>'),
        ('profit_max_graph_45_2q.html', '#7 Profit Max P=45-2Q', 'Profit = TR - TC = $240 - $60 = <strong>$180</strong></p>\n</div>\n</div>'),
        ('price_discrimination_table.html', '#8 Price Discrimination Table', '<li><strong>Social Welfare:</strong> Can increase (compared to single-price monopoly) but still below competitive level</li>\n</ul>\n</div>'),
        ('time_horizon_supply_elasticity.html', '#10 Time Horizon Elasticity', '<strong>Important:</strong> Elasticity is <em>not</em> the same as slope!</p>\n</div>'),
        ('debeers_monopoly_table.html', '#11 De Beers Table', 'In this scenario, De Beers will produce <strong>Q* = 100 diamonds</strong> and charge <strong>P* = $425</strong>.</p>\n</div>'),
        ('google_advertising_flow.html', '#12 Google Advertising', 'Lower costs = higher market share = more profits</p>\n</div>\n</div>'),
        ('double_shift_matrix.html', '#4 Double Shift Matrix', '<strong>When both curves shift, you need to analyze the net effect!</strong></p>\n</div>'),
    ]

    for filename, name, after in aids:
        print(f"Inserting {name}...")
        try:
            visual = read_file(filename)
            content, success = insert_after(content, after, visual)
            if success:
                print(f"  ✅ Success")
                inserted.append(name)
            else:
                print(f"  ❌ Pattern not found")
        except FileNotFoundError:
            print(f"  ❌ File not found: {filename}")
        print()

    write_file(guide_path, content)

    print("=" * 70)
    print(f"SUMMARY: {len(inserted)}/10 visual aids inserted")
    print("=" * 70)
    for name in inserted:
        print(f"  ✓ {name}")

if __name__ == '__main__':
    main()
