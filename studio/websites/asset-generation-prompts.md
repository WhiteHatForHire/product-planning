---
title: "ASSET GENERATION PROMPTS"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/Websites/Symposiumstudios.ai/ASSET_GENERATION_PROMPTS.docx"
status: reference
privacy: private/internal
tags:
  - website
---

# ASSET GENERATION PROMPTS

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ASSET_GENERATION_PROMPTS.md

Four standalone prompts for ChatGPT (GPT-4o or o3). Use code-generation mode, not image generation. Favicons: ChatGPT produces SVG code. OG images: ChatGPT produces a self-contained HTML file you open in a browser and screenshot at 1200x630px.

PROMPT 1: marcus-vale.com Favicon

You are producing an SVG favicon for marcus-vale.com. This is the public

thesis site for Marcus Vale, a writer and systems thinker on AI-native

systems and human judgment. The aesthetic is neo-classical Greek revival:

restrained, literary, editorial.

OUTPUT

A single SVG file, square format (viewBox="0 0 32 32"), suitable for use

as a favicon at 16x16 and 32x32, and as an Apple touch icon at 180x180.

Output raw SVG code only. No commentary, no explanation, no markdown

wrapping, no filler text.

DESIGN SPECIFICATION

Mark: The letter M as a monogram, rendered in an elegant literary serif.

Target style: Cormorant Garamond or EB Garamond. If font embedding in SVG

is unreliable, render the letter as a clean geometric path rather than a

font reference. Do not use "MV" — too crowded at small sizes. Use only "M."

Colors (light version, primary):

- Background: warm ivory (#F7F3EC)

- Letter: near-black (#171513)

Colors (dark version, secondary):

- Background: near-black (#171513)

- Letter: warm ivory (#F7F3EC)

Produce both versions in the same file as separate named groups or as two

separate SVG blocks, clearly labeled.

Decorative rule: Optional. A single thin horizontal line above and below

the letter, suggesting a classical inscription tablet. If it makes the

mark look cluttered at small sizes, remove it.

Accent color (muted gold #A8884B) may be used for the optional rule only,

not for the letter itself.

STRICT RULES

- No gradients

- No drop shadows

- No neon effects

- No rounded startup-style corners

- No abstract shapes unrelated to the letter

- Pixel-clean at 16x16

The favicon should feel like a private library bookplate, not a startup logo.

PROMPT 2: marcus-vale.com OG Image

You are producing an Open Graph link preview image for marcus-vale.com

as a self-contained HTML file. When opened in a browser and screenshotted

at exactly 1200x630px, this file becomes the final asset.

OUTPUT

A complete, self-contained HTML file. No external dependencies except

Google Fonts (loaded via link tag). All styles in a style block or inline.

No JavaScript. Output the raw HTML file only. No commentary, no explanation,

no markdown wrapping, no filler text.

CANVAS

Width: 1200px. Height: 630px. Set on the body element with overflow hidden.

COLORS

- Background: warm ivory (#F7F3EC)

- Primary text: near-black (#171513)

- Accent line: muted gold (#A8884B)

- Secondary text (URL, descriptor): near-black at 70% opacity, or stone (#7A7164)

FONTS

Load from Google Fonts:

- Cormorant Garamond (weights: 300, 400) for the name

- Inter (weights: 400) for the descriptor and URL

CONTENT (use verbatim, do not rewrite or summarize)

Name: Marcus Vale

Descriptor: Essays and field notes on how AI changes work, judgment,

software, and the size of the team required to build serious things.

URL: marcus-vale.com

LAYOUT

- Left-aligned text composition

- Top padding: 90px

- Left padding: 90px

- Right padding: 90px (leave breathing room, do not crowd)

- Name ("Marcus Vale") in Cormorant Garamond, 88px, weight 300,

letter-spacing 0.04em, near-black, on its own line

- Accent line: a thin horizontal rule (1px, muted gold #A8884B), full

content width, 24px below the name and 24px above the descriptor

- Descriptor text in Inter 400, 28px, stone (#7A7164) or near-black at

65% opacity, line-height 1.5, max-width ~900px

- URL in Inter 400, 18px, stone (#7A7164) or near-black at 45% opacity,

positioned at the bottom-left: bottom 60px, left 90px

OPTIONAL DECORATIVE ELEMENT

A single horizontal Greek meander (key fret) border element, running

across the bottom edge of the canvas or along the top edge. Render it

as an SVG pattern embedded in the HTML. Use muted gold (#A8884B) at 30%

opacity. Width of the meander pattern: 24px tall. If it makes the image

look cluttered, remove it entirely. Restraint is correct.

STRICT RULES

- No gradients

- No drop shadows

- No neon effects

- No centered text (left-aligned only)

- No hero photograph or illustration

- No more than two typefaces

- No exclamation points in copy

- No em dashes in copy

- The image must not look like a startup social media post or a guru

personal brand card. It should feel like a literary journal's cover

card or a serious writer's press kit.

PROMPT 3: symposiumstudios.ai Favicon

You are producing an SVG favicon for symposiumstudios.ai. This is the

business surface for Symposium Studios, a senior-led software studio.

The aesthetic is architectural, precise, and contemporary with a restrained

classical influence. The feel is architecture firm, not startup.

OUTPUT

A single SVG file, square format (viewBox="0 0 32 32"), suitable for use

as a favicon at 16x16 and 32x32, and as an Apple touch icon at 180x180.

Output raw SVG code only. No commentary, no explanation, no markdown

wrapping, no filler text.

DESIGN SPECIFICATION

Mark: Choose the stronger of these two options and produce it.

Option A (typographic):

The letter S as a monogram, rendered in clean modern sans-serif geometry.

Target style: Inter Display or similar geometric sans. Straight stroke

weight, no rounded terminals, slight letter-spacing. If font embedding

in SVG is unreliable, render as a clean geometric path.

Option B (symbolic):

A simplified column capital mark: two vertical strokes for the shaft,

a thin horizontal line at the top (capital) and a thin horizontal line

at the bottom (base). Reduced to its most abstract, minimal form. No

decoration. The mark should read as a column at 32x32.

Choose whichever produces the cleaner, more distinctive favicon. If

uncertain, produce both and label them.

Colors (dark version, primary):

- Background: near-black (#171513)

- Mark: warm ivory (#F7F3EC)

- Optional accent detail: stone (#7A7164)

Colors (light version, secondary):

- Background: warm ivory (#F7F3EC)

- Mark: near-black (#171513)

- Optional accent detail: stone (#7A7164)

Produce both versions in the same file as separate named groups or as two

separate SVG blocks, clearly labeled.

STRICT RULES

- No gradients

- No drop shadows

- No neon effects

- No rounded startup-style mark shapes

- No abstract tech company symbols

- Pixel-clean at 16x16

The favicon should feel like an architect's project stamp, not a startup logo.

PROMPT 4: symposiumstudios.ai OG Image

You are producing an Open Graph link preview image for symposiumstudios.ai

as a self-contained HTML file. When opened in a browser and screenshotted

at exactly 1200x630px, this file becomes the final asset.

OUTPUT

A complete, self-contained HTML file. No external dependencies except

Google Fonts (loaded via link tag). All styles in a style block or inline.

No JavaScript. Output the raw HTML file only. No commentary, no explanation,

no markdown wrapping, no filler text.

CANVAS

Width: 1200px. Height: 630px. Set on the body element with overflow hidden.

COLORS

- Background: near-black (#171513)

- Primary text: warm ivory (#F7F3EC)

- Accent line: stone (#7A7164) or muted gold (#A8884B)

- Descriptor text: warm ivory at 65% opacity, or stone (#7A7164)

- URL: warm ivory at 40% opacity

FONTS

Load from Google Fonts:

- Inter (weights: 500, 400) for all text

CONTENT (use verbatim, do not rewrite or summarize)

Name: Symposium Studios

Descriptor: Senior-led development for prototypes, product systems,

and LLM-integrated applications.

URL: symposiumstudios.ai

LAYOUT

- Left-aligned text composition

- Top padding: 90px

- Left padding: 90px

- Right padding: 90px

- Name ("Symposium Studios") in Inter 500, 76px, letter-spacing 0.02em,

warm ivory (#F7F3EC), on its own line

- Accent line: a thin horizontal rule (1px, stone #7A7164 or muted gold

#A8884B), full content width, 28px below the name and 28px above the

descriptor

- Descriptor text in Inter 400, 27px, warm ivory at 60% opacity,

line-height 1.5, max-width ~880px

- URL in Inter 400, 17px, warm ivory at 38% opacity, positioned at

bottom-left: bottom 60px, left 90px

OPTIONAL DECORATIVE ELEMENT

Either of the following, but not both:

A) A single thin vertical line (1px, stone #7A7164 at 25% opacity)

running the full height of the canvas, positioned 80px from the right

edge. This creates an architectural grid reference.

B) A simplified column capital SVG mark (two vertical strokes, thin

horizontal top and base) in the bottom-right corner, stone color at

20% opacity, approximately 60px tall.

If either element makes the image look busy, remove it. The background

darkness already carries authority. Restraint is correct.

STRICT RULES

- No bright gradients (a very subtle radial vignette from #1A1512 at

the edges to #171513 at center is acceptable if it adds depth)

- No neon glow effects

- No left-aligned startup "AI company" aesthetic

- No hero photograph or illustration

- No more than one typeface

- No exclamation points in copy

- No em dashes in copy

- The image must not look like a generic dark-mode SaaS preview card.

It should feel like an architecture firm's project announcement or a

serious product studio's identity card.
