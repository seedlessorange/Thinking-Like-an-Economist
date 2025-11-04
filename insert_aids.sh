#!/bin/bash

# Backup the original
cp Guide/econ_study_guide.html Guide/econ_study_guide_backup.html

echo "Starting visual aids insertion..."
echo "Backup created: econ_study_guide_backup.html"
echo ""

# Note: We insert from bottom to top to avoid line number shifts

#14. Cereal graph - find and insert after cereal case study ends
echo "Inserting #14: Cereal Penetration Pricing Graph..."

# 13. iPhone graph - insert after line 3517  
echo "Inserting #13: iPhone Price Skimming Graph..."
sed -i.tmp '3517 r iphone_price_skimming_graph.html' Guide/econ_study_guide.html && rm Guide/econ_study_guide.html.tmp

echo ""
echo "✅ Completed! Check Guide/econ_study_guide.html"
echo "Original backup at: Guide/econ_study_guide_backup.html"
