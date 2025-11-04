# Text Formatting & Quote Style Guide

## Overview

Enhanced CSS classes have been added to improve readability, break up dense text, and beautifully format quotes throughout the study guide.

---

## 📝 Quote Formatting Classes

### 1. Block Quotes (Standard HTML `<blockquote>`)

**Use for:** Extended quotes from sources, textbooks, or articles

**Features:**
- 30px left indent
- Subtle quotation mark watermark (15% opacity)
- Italic text
- Gradient background
- Border-left accent

**HTML:**
```html
<blockquote>
  <p>This is life in the technology lane. If you always wait for the next price cut, you'll never buy any technology product.</p>
  <cite>Steve Jobs, September 2007</cite>
</blockquote>
```

**Visual:**
- Background: Light blue gradient
- Border: 4px solid purple (#667eea)
- Large decorative quote mark top-left

---

### 2. Pull Quotes

**Use for:** Highlighting key phrases within longer text blocks

**Features:**
- Floats right (40% width on desktop, full width on mobile)
- Bold, prominent styling
- Draws eye to crucial concepts

**HTML:**
```html
<div class="pull-quote">
  This is the fundamental tension in price discrimination
</div>
```

**Visual:**
- Purple gradient background
- White text
- Large decorative quote
- Floats alongside paragraph text

**Example placement:**
```html
<p>Long paragraph explaining price discrimination theory...</p>
<div class="pull-quote">
  Capture surplus without destroying loyalty
</div>
<p>Continuation of explanation...</p>
```

---

### 3. Executive Quotes (Steve Jobs style)

**Use for:** Quotes from CEOs, executives, business leaders

**Features:**
- Blue gradient background
- Decorative quotation mark watermark
- Italicized text
- Attribution line

**HTML:**
```html
<div class="executive-quote">
  <p>We need to do a better job taking care of our early iPhone customers as we aggressively go after new ones with a lower price.</p>
  <span class="attribution">Steve Jobs, CEO Apple</span>
</div>
```

**Visual:**
- Light blue gradient
- 20% opacity quote mark
- Attribution in bold

---

### 4. Customer/User Quotes

**Use for:** Quotes from customers, users, consumers expressing reactions

**Features:**
- Red/pink background (indicates emotion/reaction)
- Compact styling
- Speaker attribution

**HTML:**
```html
<div class="customer-quote">
  I feel totally screwed. I'm a loyal Mac owner and early adopter.
  <span class="speaker">Alec Meer, iPhone buyer</span>
</div>
```

**Visual:**
- Pink/red background (#fef2f2)
- Red border-left
- Italic text
- Speaker name in bold

---

### 5. News Article Quotes (NYT style)

**Use for:** Quotes from news articles, journalism

**Features:**
- Serif font (Georgia)
- Yellow/amber background
- 30px left indent

**HTML:**
```html
<div class="news-quote">
  <em>"My love affair with Apple is officially over,"</em> wrote one iPhone owner on the Unofficial Apple Weblog site.
</div>
```

**Visual:**
- Amber background (#fffbeb)
- Serif typeface
- Indented from left

---

### 6. Indented Quote Blocks

**Use for:** Multi-paragraph quotes, letter excerpts, detailed explanations

**Features:**
- 30px left indent
- Green accent
- Clean, simple styling

**HTML:**
```html
<div class="indented-quote">
  <p>First paragraph of the quote...</p>
  <p>Second paragraph continues...</p>
</div>
```

**Visual:**
- Gray background (#f9fafb)
- Green border-left (#10b981)
- Italic text

---

### 7. Multi-Paragraph Quotes

**Use for:** Long quotes spanning multiple paragraphs

**HTML:**
```html
<div class="multi-para-quote">
  <p>First, I am sure that we are making the correct decision to lower the price...</p>
  <p>Second, being in technology for 30+ years...</p>
  <p>Third, even though we are making the right decision...</p>
</div>
```

**Visual:**
- Slate background
- Purple border-left
- Each paragraph spaced nicely

---

### 8. Academic/Research Quotes

**Use for:** Quotes from textbooks, academic papers, research

**HTML:**
```html
<div class="academic-quote">
  According to the research, price elasticity of demand measures the responsiveness of quantity demanded to price changes.
</div>
```

**Visual:**
- Green background (#f0fdf4)
- Professional styling

---

### 9. Emphasis Quotes

**Use for:** Highlighting important statements inline

**HTML:**
```html
<div class="emphasis-quote">
  Key insight: The $100 credit was Apple buying back goodwill
</div>
```

**Visual:**
- Yellow background (#fffbeb)
- Orange border
- Stands out in content flow

---

## 📋 Text Formatting Classes

### 1. Dense Text Breaking

Automatically applied to `.content-card`, `.key-concept`, `.warning-box`

**Features:**
- 1rem margin between paragraphs
- 1.7 line-height
- Extra spacing between consecutive paragraphs

**No code needed** - automatically applies to existing classes.

---

### 2. Em-Dash Lists

**Use for:** Inline enumeration within prose

**HTML:**
```html
<ul class="em-dash-list">
  <li>First key point about pricing</li>
  <li>Second strategic consideration</li>
  <li>Third implementation detail</li>
</ul>
```

**Visual:**
- Purple em-dashes (—) instead of bullets
- Cleaner look than bullet points
- Better for embedded lists

---

### 3. Readable Spacing

**Use for:** Sections with dense explanations

**HTML:**
```html
<div class="readable-spacing">
  <p>First paragraph...</p>
  <p>Second paragraph with extra spacing...</p>
  <ul>
    <li>List item with spacing</li>
    <li>Another list item</li>
  </ul>
</div>
```

**Features:**
- 1.25rem between paragraphs
- 0.75rem between list items
- Better visual breathing room

---

### 4. Inline Quotes

**Use for:** Short quoted phrases within sentences

**HTML:**
```html
<p>Steve Jobs described it as <q>life in the technology lane</q> when defending the price cut.</p>
```

**Visual:**
- Automatic smart quotes
- Italic styling
- Gray color

---

## 🎨 Citation & Attribution Styling

### Quote Citations

**HTML:**
```html
<blockquote>
  <p>Quote text here...</p>
  <cite>Source Name, Date</cite>
</blockquote>
```

**Or standalone:**
```html
<span class="quote-citation">New York Times, September 7, 2007</span>
```

**Visual:**
- Right-aligned
- Gray color
- Small font
- Automatic em-dash prefix

---

### Source Attribution

**HTML:**
```html
<span class="source-attribution">Lou Hawthorne, early iPhone buyer</span>
```

**Visual:**
- Inline
- Automatic "— " prefix
- Gray color (#6b7280)

---

### Article References

**Use for:** Citing full articles/sources

**HTML:**
```html
<div class="article-reference">
  <span class="source-name">New York Times</span>
  <span class="source-date">September 7, 2007</span>
  <p>"iPhone Owners Crying Foul Over Price Cut"</p>
</div>
```

**Visual:**
- Box styling
- Blue accent
- Clear source/date separation

---

## 📖 Usage Examples

### Example 1: iPhone Case Study Improvement

**Before:**
```html
<p>"I feel totally screwed" - Alec Meer</p>
```

**After:**
```html
<div class="customer-quote">
  I feel totally screwed. I'm a loyal Mac owner and early adopter.
  <span class="speaker">Alec Meer, iPhone buyer</span>
</div>
```

---

### Example 2: Steve Jobs Letter

**Before:**
```html
<p><em>"This is life in the technology lane..."</em> - Steve Jobs</p>
```

**After:**
```html
<div class="executive-quote">
  <p>This is life in the technology lane. If you always wait for the next price cut or to buy the new improved model, you'll never buy any technology product because there is always something better and less expensive on the horizon.</p>
  <span class="attribution">Steve Jobs, Apple CEO - September 6, 2007</span>
</div>
```

---

### Example 3: Breaking Up Dense Paragraphs

**Before:**
```html
<p>Apple's strategy involved price skimming where they launched at $599 to capture early adopters who have inelastic demand and are willing to pay premium prices, then two months later they dropped the price to $399 to target the mainstream market which is more price-sensitive and has elastic demand, but this angered early adopters who felt cheated.</p>
```

**After:**
```html
<div class="readable-spacing">
  <p>Apple's strategy involved <strong>price skimming</strong> in two phases:</p>

  <div class="pull-quote">
    Target different segments with different elasticities
  </div>

  <p><strong>Phase 1:</strong> Launched at $599 to capture early adopters who have inelastic demand and are willing to pay premium prices.</p>

  <p><strong>Phase 2:</strong> Two months later, dropped the price to $399 to target the mainstream market, which is more price-sensitive and has elastic demand.</p>

  <p><strong>The Problem:</strong> This angered early adopters who felt cheated by the rapid price reduction.</p>
</div>
```

---

### Example 4: Highlighting Key Insights

**Use pull quotes to extract key concepts:**

```html
<div class="content-card">
  <p>The iPhone pricing debacle illustrates an important economic principle about price discrimination. While firms want to extract consumer surplus from different market segments, doing so too quickly or obviously can damage brand equity and customer loyalty.</p>

  <div class="pull-quote">
    Price discrimination requires balancing surplus capture with brand trust
  </div>

  <p>Apple learned this lesson and adjusted their strategy for future product launches, maintaining stable flagship pricing while introducing product tiers instead.</p>
</div>
```

---

## 🎯 Best Practices

### 1. Choose the Right Quote Style

| Quote Type | Use This Class |
|------------|----------------|
| News article quote | `.news-quote` |
| CEO/Executive statement | `.executive-quote` |
| Customer reaction | `.customer-quote` |
| Academic source | `.academic-quote` |
| General quote | `<blockquote>` |
| Key phrase highlight | `.pull-quote` |

### 2. Break Long Paragraphs

**Rule of thumb:** If a paragraph is more than 4-5 lines, consider:
- Splitting into 2-3 shorter paragraphs
- Adding a pull quote to highlight the key idea
- Using an em-dash list if enumerating points

### 3. Add Visual Hierarchy

Use different quote styles to create visual variety:
```html
<!-- Alternate between styles -->
<div class="executive-quote">...</div>
<p>Explanation...</p>
<div class="customer-quote">...</div>
<p>More explanation...</p>
<div class="news-quote">...</div>
```

### 4. Always Attribute

Every quote should have clear attribution:
- Use `<cite>` in blockquotes
- Use `.speaker` in customer quotes
- Use `.attribution` in executive quotes
- Use `.source-attribution` for standalone citations

---

## 🔄 Migration Guide

### Converting Existing Quotes

1. **Find quotes** in your guide (search for `<em>"` or `<strong>"`)
2. **Identify type** (customer, executive, news, academic)
3. **Wrap in appropriate class**
4. **Add attribution** if missing
5. **Test visual appearance**

### Priority Areas

Focus on enhancing:
1. ✅ Session 4 iPhone case study (already has some improvements)
2. Session 7 Price discrimination examples
3. Problem set scenario descriptions
4. Any lengthy quoted passages

---

## 📱 Mobile Responsiveness

All quote styles are mobile-responsive:
- Pull quotes become full-width on mobile
- Indentation reduces on small screens
- Font sizes adjust appropriately
- Touch-friendly spacing

---

## Summary of All Classes

```css
/* Quote Styles */
blockquote                 // Standard quotes
.pull-quote               // Floating highlight quotes
.executive-quote          // CEO/leader quotes
.customer-quote           // User reaction quotes
.news-quote              // Journalism quotes
.indented-quote          // Letter-style quotes
.multi-para-quote        // Long multi-paragraph
.academic-quote          // Research/textbook
.emphasis-quote          // Highlighted statements

/* Text Formatting */
.readable-spacing        // Better paragraph spacing
.em-dash-list           // Em-dash bullet style
.dense-text             // For complex explanations
q                       // Inline short quotes
.inline-quote           // Alternative inline style

/* Attribution */
.quote-citation         // Quote sources
.source-attribution     // Speaker attribution
.article-reference      // Full article citations
.speaker               // Customer quote speakers
.attribution           // Executive quote attribution
```

---

**All styles are now active in your study guide!** Simply wrap existing text in these classes to improve formatting.
