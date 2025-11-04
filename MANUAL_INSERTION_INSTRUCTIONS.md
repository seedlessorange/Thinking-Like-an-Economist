# Manual Visual Aids Insertion Instructions

## Status: 3 of 14 Inserted

### ✅ Already Inserted (via script):
- #9: Competition Spectrum Diagram
- #13: iPhone Price Skimming Graph
- #14: Cereal Penetration Pricing Graph

### 📋 Remaining 11 Visual Aids - Insert Manually

Use your IDE's "Go to Line" feature (Cmd+G in VS Code) to navigate to these locations.

---

## Session 2: Elasticity (Lines ~1700-1900)

### #3: Elasticity Comparison Graph
**File:** `elasticity_comparison.html`
**Where:** After the elastic/inelastic concept cards, before worked examples
**How to find:**
1. Search for: "Elastic vs. Inelastic: What's the Difference"
2. Scroll down past the two cards (Elastic and Inelastic)
3. Look for the next `<div class="content-card">` or `<h3>` tag
4. Insert the entire contents of `elasticity_comparison.html` BEFORE that next section

### #6: Elasticity Reference Table
**File:** `elasticity_reference_table.html`
**Where:** After all elasticity discussions in Session 2, as comprehensive reference
**How to find:**
1. Search for: "Price elasticity of supply (PES)"
2. Find where the elasticity section ends (look for closing `</div>` tags)
3. Insert before the next major section starts

### #10: Time Horizon Supply Elasticity
**File:** `time_horizon_supply_elasticity.html`
**Where:** In Session 2, showing momentary/short-run/long-run differences
**How to find:**
1. Search for: "elasticity"
2. Find a good spot in Session 2 after basic elasticity concepts
3. Insert before moving to next major topic

---

## Session 4/5: Costs and Supply (Lines ~4000-5000)

### #2: LRAC Curve
**File:** `lrac_curve.html`
**Where:** After the diseconomies of scale warning box
**Current line ~4978:** Contains "diseconomies of scale"
**How to find:**
1. Go to line 4978
2. Look for the warning box about diseconomies of scale
3. Find the closing `</div>` tags for that warning box
4. Insert the LRAC curve visualization RIGHT AFTER those closing tags

---

## Session 6: Markets & Monopolies (Lines ~5300-6500)

### #1: Market Structure Comparison Table
**File:** `market_structure_table.html`
**Current line 5319:** "Part 1: Highly Competitive Markets"
**Where:** Right BEFORE line 5319
**How to find:**
1. Go to line 5319
2. You'll see: `<span>Part 1: Highly Competitive Markets (Perfect Competition)</span>`
3. Scroll UP to find where "The Competition Spectrum" section ENDS
4. Insert the Market Structure Table between the Competition Spectrum and Part 1

### #7: Profit Maximization Graph P=45-2Q
**File:** `profit_max_graph_45_2q.html`
**Where:** After profit maximization example explanation in Session 6
**How to find:**
1. Search for: "P = 45 - 2Q"
2. Find the worked example showing Q* = 8.75, P* = 27.5
3. Insert the visual aid RIGHT AFTER that example's closing `</div>` tags

### #11: Enhanced De Beers Monopoly Pricing Table
**File:** `debeers_monopoly_table.html`
**Where:** In Session 6 or 7, showing monopoly profit maximization
**How to find:**
1. Search for: "De Beers"
2. Find where De Beers example is discussed
3. Insert after the textual explanation ends

---

## Session 7/8: Price Discrimination & Two-Sided Markets (Lines ~6500+)

### #8: Price Discrimination Comparison Table
**File:** `price_discrimination_table.html`
**Where:** After the three degrees of price discrimination examples
**How to find:**
1. Search for: "first degree" or "1st degree"
2. Find where all three degrees are explained
3. Insert comprehensive table AFTER those explanations

### #12: Google Advertising Flow Diagram
**File:** `google_advertising_flow.html`
**Where:** In Session 7 or 8, illustrating two-sided market platform
**How to find:**
1. Search for: "Google" or "two-sided market"
2. Find where Google/platform economics is discussed
3. Insert the flow diagram right after that section

---

## Problem Sets

### #4: Double Shift Decision Matrix
**File:** `double_shift_matrix.html`
**Where:** In PS1 near double shift discussions, OR in Session 2 comparative statics
**How to find:**
1. Search for: "double shift" or "both curves shift"
2. Insert the decision matrix right after that discussion
3. Alternative: Put it in Session 2 after supply/demand shift basics

---

## Step-by-Step Process:

1. **Open the file** you want to insert (e.g., `market_structure_table.html`)
2. **Select ALL content** (Cmd+A)
3. **Copy** (Cmd+C)
4. **Open** `Guide/econ_study_guide.html`
5. **Find the insertion point** using the instructions above
6. **Position cursor** at the exact insertion line
7. **Paste** (Cmd+V)
8. **Add blank lines** before/after for spacing if needed
9. **Save** (Cmd+S)
10. **Repeat** for next visual aid

---

## Tips:

- **Work from bottom to top** of the document to avoid line number shifts
- **Test in browser** after inserting a few to ensure layout works
- **Keep the backup** files in case you need to revert
- **Use Find** (Cmd+F) liberally to locate exact text mentioned above
- **Look for section headings** like `<h3>` tags to orient yourself

---

## Quick Reference - Files to Insert:

```
Remaining 11 files:
├── market_structure_table.html (Session 6)
├── lrac_curve.html (Session 5)
├── elasticity_comparison.html (Session 2)
├── double_shift_matrix.html (Session 2 or PS1)
├── elasticity_reference_table.html (Session 2)
├── profit_max_graph_45_2q.html (Session 6)
├── price_discrimination_table.html (Session 7)
├── time_horizon_supply_elasticity.html (Session 2)
├── debeers_monopoly_table.html (Session 6/7)
└── google_advertising_flow.html (Session 7/8)
```

---

## Verification:

After inserting all, search the guide for these strings to verify insertion:
- "📊 Market Structure Comparison Table"
- "⏱️ Supply Elasticity Across Time Horizons"
- "📱 iPhone 2007: Price Skimming" (already inserted ✓)
- "🥣 New Cereal Brand: Penetration Pricing" (already inserted ✓)
- "🔄 The Competition Spectrum" (already inserted ✓)

---

**Total when complete: 14/14 visual aids inserted** 🎉
