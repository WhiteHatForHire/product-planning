---
title: "Dialectical Combat Visual Design System v2"
source_archive: "Phronetics"
source_path: "##Phronetics/AI Engine/Dialectical_Combat_Visual_Design_System_v2.docx"
status: active
privacy: private/internal
tags:
  - theory
---

# Dialectical Combat Visual Design System v2

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Table of Contents

DIALECTICAL COMBAT

Visual Design System, v2

Marcus Vale | Internal Only | May 2026

Companion to: Dialectical Combat Master Spec v2

Status: Final MVP-0 Build Spec

What Changed From v1

A concise change log. Each change is load-bearing. None is cosmetic.

Score numeral count-up cut. The 48px mono numeral that counted from 0 to N over 800ms is replaced. Each virtue card now leads with the evidence quote at full reading weight; the 0-10 score appears below as quiet metadata in 14px mono. The only counting animation in v1 has been removed. The post-match no longer contradicts the spec’s evidence-not-verdict thesis at the moment of greatest user impact.

Token streaming for Foe responses removed. Full-statement fade-in always. Streaming was metaphor-incoherent (Aristotle does not type) and produced visible kerning judder in serif type during real-time rendering. Streaming may continue in the backend for latency; rendering is always full-statement fade.

HP rule depletion now uses length plus saturation. The hairline visibly shortens as well as fading. Resolves the perceptual signal failure where 2px saturation-only fade was too subtle to register peripherally. Mobile rules increased to 3px; desktop remains 2px.

Free-font fallback tier added. Between the canonical Klim stack and the system fallback, an intentional production-safe tier is specified: Source Serif 4, Inter, IBM Plex Mono. The premium stack becomes enhancement; the free tier is the genuine production target without licensing.

Mobile composition mode added. Tapping the input on small viewports opens a full-screen composer with the contested ground pinned at top. Replaces the fixed-bottom expanding textarea pattern that broke under mobile keyboard interaction.

Tablet layout (768 to 1023px) defined explicitly. 600 to 640px content column, inline marginalia (mobile pattern), no right-margin treatment. Closes the gap that v1 left undefined between mobile and desktop breakpoints.

“No conventional buttons” softened to “semantic controls styled as text.” Real semantic <button> elements with discreet hover, focus, and pointer affordances. Preserves the visual register while restoring discoverability and keyboard operability.

First-match orientation screen added for MVP-0. A single one-time intro before the user faces Aristotle. Stored in localStorage, never repeats. The manuscript register holds; the floor of orientation is paid.

Accessibility section made first-class. New Part VIII covers semantic HTML, focus states, ARIA live regions, reduced-motion behavior, contrast thresholds, browser zoom, tap targets, and low-vision considerations. The opinionated minimalism creates accessibility obligations that v1 had not paid.

Internationalization scope locked. MVP-0 and V1 are English-only across all dialogue. Multi-script typesetting (Greek, Chinese, Arabic) deferred to V2 with Noto-family fallbacks defined.

Ceremonial pacing now scales with familiarity. After five completed matches, default tempo compresses automatically. Reduced motion is always honored. User-selectable swift mode arrives in V1 settings.

Quality tag treatment honest. Mono uppercase remains, but framed as restrained assessment-layer typography rather than scribal annotation. Tracking tightened from +0.08em to +0.04em, size reduced from 13px to 12px. The system stops claiming a manuscript hand it does not have.

Per-Foe ink accents not used below 16px. Transcript spine items at 14px sit in margin color throughout. Avoids contrast failures at small sizes for warm-ink Foes (Aristotle, Epicurus) where 18px AA passes but smaller sizes do not.

Functional rule color separated from decorative. A new functional rule color (#9B8D74) for input boundaries, focus states, and active affordances. The original #C9BFA8 is preserved for decorative dividers only. Resolves the 1.57:1 contrast failure on input affordances.

Misclick protection on rematch. Tapping “Begin again” opens a 2-second cancel window before the new match begins. The only confirmation pattern in the product. Exists because rematch is irreversible and accidental taps lose the entire post-match.

Design Thesis

The product looks like a serious contemporary edition of a serious old text. Not a re-enactment. An inheritance.

The Foe speaks in the historical hand. The reader writes back in their own contemporary voice. Both inhabit the same warm parchment surface. The transcript is a manuscript being inscribed, not a chat log being filled.

Combat is the surface. Dialectical arete is the engine. The visual system honors both: the gravity of philosophical exchange and the tension of contested ground. HP exists as ground eroding, not as wounds. Damage exists as pressure on the page, not as violence. Score exists as quiet provisional metadata, not as climactic reveal.

The product moves the way ink moves on paper. It also opens the way a book opens: predictable, accessible, ready for use. The manuscript register disciplines the interface. It does not dominate it. The product can be perceived, operated, and returned to.

Part I. Core Principles

Ten load-bearing decisions. Every visual choice in the system serves at least one of these. Choices that conflict get cut, not compromised.

Manuscript register, Rams discipline. Warm parchment, ink, marginalia for assessment annotations. Executed with Braun-1960s restraint to prevent drift into LARP. The product reads as a serious contemporary edition of an old text.

Typography does the heaviest lifting. Approximately 70% of the visual identity is type. Spacing carries another 20%. Color does almost no semantic work. The product communicates through hierarchy and register, not through ornament.

No game vocabulary in visual language. No HP fills, no damage numbers, no critical-hit treatments, no celebration animations, no level-up sparkle. HP depletes by ground eroding (length plus saturation). Damage is felt as pressure. Outcomes are sensed, not announced. Score is metadata, not climax.

Foe and player typographically distinct. Foe in serif, in their own warm ink. Player in sans, in neutral charcoal. Different cognitive modes earn different visual treatments.

System coherence over per-Foe theming. Each Foe receives one warm ink tone for their text only. The arena (parchment, layout, UI) stays stable across all Foes. The Foe changes the light; the room does not redesign itself. Color is voice register, never identity carrier.

Light parchment by default. Dark mode arenas signal game more than serious instrument. Dark mode becomes a V2 user setting using the same warm logic, never the canonical mode.

Quiet motion only, with reduced-motion respected. Kinetic where it carries meaning. No bouncing, no spring physics, no Lottie celebrations. HP depletion is slow. The Mirror Move transition is ceremonial. Everything else fades. When a user prefers reduced motion, all transitions collapse to instant or near-instant.

Mirror Move is the inflection point. The single moment in the product that earns dramatic visual treatment. The match transcript dims to near-black. A blank parchment surface rises. The prompt sits in display serif. The textarea is the only thing that exists. Everything else in the product serves this moment.

Semantic controls styled as text. Visual treatment without conventional buttons. But every actionable element is a real semantic <button> or appropriate semantic control with proper accessibility attributes, visible focus, and discreet affordance (pointer cursor, faint underline on hover or focus). Visual purity does not justify hostile UX or broken accessibility.

Restraint serves the user. Where the manuscript register and the user’s ability to perceive, operate, or return are in tension, the user wins. The metaphor disciplines the interface; it does not replace usability.

Part II. Typography

Type Stack

Three tiers: canonical premium, production-safe fallback, system fallback. The CSS font-family declaration proceeds in this order.

Canonical Premium Stack (Klim license required)

Display face (Foe claims, screen headers): Tiempos Headline (Klim Type Foundry)

Reading face (Foe text, transcript body): Tiempos Text (Klim Type Foundry)

Player face (player text, input): Söhne (Klim Type Foundry)

Label face (assessment annotations): GT America Mono (Grilli Type)

Production-Safe Fallback (free, open source)

This is the genuine production target if Klim licensing is not in place. Each fallback approximates the canonical face’s register without licensing risk.

Display fallback: Source Serif 4 (Adobe, OFL)

Reading fallback: Source Serif 4 (body weights)

Player fallback: Inter (Rasmus Andersson, OFL)

Label fallback: IBM Plex Mono (IBM, OFL)

The free fallback tier is intentional, not accidental. Source Serif 4 carries the modern proportions and authoritative weight that Tiempos provides. Inter handles humanist sans warmth. IBM Plex Mono is a clean monospace at small sizes.

System Fallback (last resort)

Display/Reading: Hoefler Text, Iowan Old Style, Georgia, serif

Player: -apple-system, Segoe UI, Roboto, sans-serif

Label: ui-monospace, SF Mono, Consolas, monospace

The system fallback is the floor. The product still functions. The register softens.

Font Loading

font-display: swap for all faces. Critical fonts (Reading and Player) preloaded via <link rel="preload"> in the document head. Custom font subsets shipped to reduce payload (Latin Extended-A only for MVP-0 and V1; multi-script subsets in V2).

Font metrics matched between Source Serif 4 and Tiempos Text using size-adjust, ascent-override, and descent-override to minimize cumulative layout shift on font swap. The opening claim must not visibly reflow when the canonical font loads.

Type Scale

Single scale across the product. Mobile values listed first; desktop values increase proportionally as noted.

Display face (Tiempos Headline / Source Serif 4)

Foe Opening Claim: clamp(22px, 7vw, 26px) mobile, 32px / 40px line desktop

Match Start Header: 20px / 28px line mobile, 24px / 32px line desktop

Mirror Move Prompt: 24px / 32px line mobile, 28px / 36px line desktop

Virtue Dimension Name: 20px / 28px line (reduced from 28px in v1; now meta, not headline)

Section Headers: 20px / 28px line

Reading face (Tiempos Text / Source Serif 4)

Foe Statements: 18px / 30px line mobile, 20px / 32px line desktop

Evidence Quote (post-match): 18-20px / 28px line, italic, headline visual element on virtue cards

Transcript Spine Item: 14px / 22px line (collapsed)

Player face (Söhne / Inter)

Player Responses: 18px / 30px line mobile, 20px / 32px line desktop

Input Field: 18px / 30px line mobile, 20px / 32px line desktop

Label face (GT America Mono / IBM Plex Mono)

Quality Tag: 12px / 16px line, +0.04em letter-spacing, uppercase (revised from 13px / +0.08em in v1)

Exchange Number: 12px / 16px line, +0.04em, uppercase

Section Label: 13px / 18px line, +0.08em, uppercase

Character Counter: 12px / 16px line

Virtue Score Numeral: 14px / 20px line, mono (revised from 48px in v1; now metadata, not climax)

Match Metadata: 14px / 20px line

Body line-height anchored at 1.6 to 1.7 across reading and player faces. Generous line-height is non-negotiable; this is a product for slow reading.

Foe vs Player Differentiation

Three signals carry the distinction. None is sufficient alone; none is dispensable.

Face: Foe in Tiempos Text serif. Player in Söhne sans.

Color: Foe in their per-Foe ink accent. Player in neutral charcoal #2A2620 always.

Alignment: Foe statements left-aligned to column edge. Player responses right-aligned with looser tracking and a thin left rule (1px, decorative rule color) marking them as the inscribed-by-the-reader layer.

Color is one signal among three. Color-blind users perceive the distinction through face and alignment alone.

Accessibility Notes for Typography

Browser zoom must work without layout breaking up to 200%. All sizes specified in px or rem; no fixed-px containers preventing text-only enlargement.

Minimum font size 14px anywhere in the product. Text weight stays in normal/medium range; no thin weights below 400 (legibility risk for low-vision users).

Per-Foe accent ink is forbidden below 16px text size. The collapsed transcript spine items at 14px sit in margin color (#6B5F4E) throughout, with no Foe accent treatment.

Part III. Color System

Core Palette

Warm parchment-and-ink. No semantic UI color. No reds for damage. No greens for success. No blues for information. The product communicates through type and space; color carries register, not signal.

Parchment (background)

Light mode: #F4EDE0

Dark mode (V2): #1C1814

Surface (raised elements: cards, post-match panels)

Light mode: #FAF6EC

Dark mode: #221E18

Ink (primary text)

Light mode: #1A1816 (warm near-black, never pure)

Dark mode: #E8DFC8

Margin (secondary text, exchange numbers, character counter)

Light mode: #6B5F4E

Dark mode: #8A7F6E

Decorative Rule (purely visual dividers, hairline ornament)

Light mode: #C9BFA8

Dark mode: #4A4238

Functional Rule (input boundaries, focus indicators, active affordance) (NEW IN V2)

Light mode: #9B8D74

Dark mode: #6B6354

The decorative/functional split exists because #C9BFA8 has only ~1.57:1 contrast against parchment. Acceptable for non-functional dividers. Insufficient for any rule the user must perceive to operate the interface. Functional rules use #9B8D74 (~3.0:1 against parchment, meets WCAG 2.4.7 for non-text contrast).

Mirror Move Backdrop

Both modes: #0E0B07 (deep ink, near-black)

Per-Foe Ink Accent

Each Foe has one warm ink tone, used only as the color of that Foe’s text. Never as UI accent color. Never as button color. Never as background. Never used at text sizes below 16px.

Foe

Hex

Description

Aristotle

#8B5A2B

warm amber-brown (the Lyceum’s ink)

Machiavelli

#2B2D3A

iron-gall blue-black (period correct)

Confucius

#3A3530

sumi grey-black

Marcus Aurelius

#5C4A38

oak gall brown

Mencius

#4A3528

russet ink

Epicurus

#6B5840

pale walnut

Ibn Rushd

#2F3A2D

deep cypress green-black

Anscombe

#1F2030

near-black with violet undertone

Player text: #2A2620 (neutral dark warm charcoal) always.

Per-Foe ink is voice register. It is not identity. Foe identity is carried by name, claim, voice, and (in V2) typographic mark, never by color alone. Color-blind users access the full system via every other signal.

Contrast Rules

All text/background combinations meet WCAG AA at the size used. Spot-checked ratios on parchment (#F4EDE0):

#1A1816 ink: ~14.2:1 (AAA at all sizes)

#2A2620 player charcoal: ~12.9:1 (AAA)

#6B5F4E margin: ~5.35:1 (AA at body size)

#8B5A2B Aristotle: ~5.0:1 (AA at >=18px only)

#6B5840 Epicurus: ~5.8:1 (AA at >=16px)

All other Foe inks: AA pass at body size

Foe accent ink is forbidden below 16px text size, with no exceptions. This includes the transcript spine items, which at 14px sit in margin color throughout.

Functional UI elements (input boundaries, focus indicators, active affordance lines) must reach 3:1 contrast against parchment background per WCAG 2.4.7. Decorative elements (dividers, hairline ornament) may go below 3:1 if they carry no operative meaning.

What Color Does Not Do

No red for damage, errors, or warnings

No green for success, gains, or positive feedback

No blue for information, links, or UI affordances

No saturated accent colors anywhere

No gradient fills

No drop shadows beyond a single soft shadow on the Mirror Move parchment surface

Damage is communicated by ground depletion, not color shift. Errors are communicated by language, not color. Affordances are communicated by typography and discreet line work, not color.

Part IV. Layout and Spacing

Spacing Scale

8px base unit. Generous throughout. The product is not dense.

xs: 8px (tight pairings)

sm: 16px (component interior padding)

md: 24px (block separation within a section)

lg: 40px (section separation)

xl: 64px (exchange separators in transcript)

2xl: 104px (post-match section spacing)

3xl: 168px (ceremonial spacing on desktop and tablet)

On mobile viewports (<= 767px), ceremonial spacing collapses responsively: clamp(64px, 18vh, 168px). This prevents the opening claim from being pushed below the fold on small screens.

Vertical rhythm anchored at 32px line-height for body. Page margins: 24px on mobile, 32px on tablet, 96px on desktop (or fluid centered with 720px max content width).

Layout Grid

Three breakpoints, all defined.

Mobile (320 to 767px)

Single column, 24px gutters

HP rules at top of viewport, fixed-position, 3px height (revised from 2px in v1 for legibility)

Foe HP rule on left half, Player HP rule on right half, 8px gap between

Foe name and exchange number on a metadata row immediately below HP rules

Transcript pane below metadata, scrollable

Quality tags inline below player turn, 16px gap

Input field NOT fixed-bottom in MVP-0 mobile. Tap on input area triggers Composition Mode (see below)

Tablet (768 to 1023px) (NEW IN V2)

Single centered column, 600 to 640px content width

32px gutters

HP rules same as mobile (3px height)

Quality tags inline (mobile pattern), not right-margin (insufficient space at this width)

Input field tap triggers Composition Mode (same as mobile)

Ceremonial spacing follows mobile responsive clamp on portrait orientation; full 168px on landscape

Desktop (1024px+)

Centered 720px column for content

HP rules 2px height (high-DPI rendering tighter)

Wide left and right margins (where marginalia would live in a real codex)

Quality tags appear in the right margin, vertically aligned to bottom of player turn. Mono uppercase, in margin color. Pure marginalia treatment.

Exchange numbers in the left gutter, mono, small, muted

Active layout container constrained to maximum 1280px (column plus side margins) on wide monitors. Background parchment extends to viewport edges; active marginalia area is bounded so it does not float in space on ultra-wide screens.

Mobile Composition Mode (NEW IN V2)

On mobile and tablet, tapping the input area opens a full-screen composition mode rather than expanding a fixed-bottom textarea.

Layout:

Background: parchment surface (same #F4EDE0)

Top: current contested ground (Foe’s most recent statement) pinned at top, in Foe’s ink, body serif, 18px. Truncated at ~3 lines if extremely long with “Read full statement” affordance to expand inline.

Middle: Player textarea, full width minus 24px gutters, expandable, 18px Söhne sans

Above keyboard (sticky): “Commit response” submit affordance in italic body serif, character counter in mono (“482 / 1000”), “Cancel” affordance in margin color italic at 14px

Behavior:

Tap “Cancel” to dismiss composer without submitting; transcript view returns

Tap “Commit response” to submit; composer dissolves over 400ms; transcript view returns; Foe response begins

Composer is the active surface during input. The transcript is not visible while typing. The player composes deliberately rather than alongside the running record.

The element that has to be perfect: the contested ground pinned at top. The player must always see what they are responding to. If that statement is hidden behind the keyboard, the entire dialectical exchange breaks.

Transcript Spine Behavior

By exchange 6 the transcript would become unwieldy if everything stayed full-fidelity. Past exchanges collapse to a single-line spine.

Current exchange: full-fidelity. Foe statement and player response at full size with full quality tag.

Previous exchange (one back): full-fidelity, slightly dimmed (margin color overlay).

Earlier exchanges: collapsed to single-line summary. Format: “EXCHANGE 03: specific contradiction found” in mono at 14px, in margin color throughout (no Foe accent at this size).

Tap or click any spine line to expand that exchange to full-fidelity inline.

If a terrain shift occurred in that exchange, the spine line includes “terrain shifted” appended to the tag.

This makes the transcript a record of pressure points rather than a scrollback swamp.

Safe Area and Keyboard Behavior

The product respects iOS and Android safe areas via env(safe-area-inset-*). The HP rules row clears the top safe area; the input affordances clear the bottom safe area.

When the soft keyboard appears (mobile/tablet composition mode), the layout uses the visual-viewport API to track the actual visible region. The composer textarea remains above the keyboard; the contested ground at top remains visible. Submit and cancel affordances remain visible above the keyboard.

Part V. Motion

Quiet product. Motion exists only where it carries meaning. The product moves the way ink moves on paper: settling, fading, pressing, never bouncing.

Default Motion

HP Depletion

Duration: 1200ms

Curve: cubic-bezier(0.22, 1, 0.36, 1) ease-out

Mechanism: Both length depletion and ink saturation fade. The rule visibly shrinks toward the gap (length is primary signal) while saturation fades on the remaining length (secondary signal).

Slight settling pause (200ms) after the curve completes before the next exchange becomes interactable.

Quality Tag Appearance

Duration: 600ms fade-in

Delay: 200ms after the Foe response settles

Mechanism: Opacity 0 to 1, no positional movement. Tag emerges in the margin like a scribe’s note being added after the exchange has been read.

Foe Response Arrival (REVISED IN V2)

Mechanism: Full-statement fade-in over 800ms after the Foe-thinking dots dissolve.

No token streaming. No typing animation. Aristotle does not type. Streaming is acceptable in the backend for latency reduction; rendering is always full-statement fade.

Terrain Shift

Label fade-in: 800ms

Position: Above the new Foe statement

Persistence: Label remains in the transcript spine when exchange collapses

Match Start (Opening Claim)

Initial pause: 1200ms blank parchment after Foe metadata appears (compresses to 400ms after 5 completed matches)

Claim fade-in: 800ms, opacity 0 to 1 (compresses to 400ms after 5 completed matches)

Input activate: Input field becomes interactable 800ms after claim completes its fade. “Your move” placeholder appears.

Match End

Active match dim: 1800ms to 30% opacity

HP completion: HP rules finish their final depletion, then dissolve

Rule fade-in: Single horizontal hairline rule fades in across the column over 800ms

Completion text: “The exchange is complete.” in display serif at 20-24px, fades in 600ms after rule

Pause: 1200ms before Mirror Move transition begins

Mirror Move Transition

Backdrop: Background transitions from parchment to deep ink (#0E0B07) over 1800ms (compresses to 800ms after 5 completed matches)

Parchment rise: Mirror parchment surface translate-y from below over 1200ms (compresses to 600ms after 5 completed matches)

Prompt fade-in: 600ms after parchment settles

Total ceremony: ~3000ms first-time; ~1200ms after compression

Virtue Card Reveal (REVISED IN V2)

Per card: 600ms total reveal (revised from 1400ms in v1)

Mechanism: All card content (dimension name, evidence quote, score numeral metadata) fades in together over 600ms. No count-up animation on the score. The quote and the number arrive simultaneously.

Advance: Manual tap or click. No auto-advance.

Skip: None within sequence.

No bouncing. No spring physics. No Lottie. No celebration animations of any kind.

Reduced Motion (prefers-reduced-motion: reduce)

When the user’s system signals reduced motion, the following overrides apply globally.

HP depletion: instant or 150ms minimum, no curve animation

Quality tag: instant fade-in, no delay

Foe response: instant appearance, no fade

Terrain shift label: instant

Match Start opening claim: instant after metadata appears, no 1200ms pause

Match End dim: instant 30% opacity, no 1800ms transition

Mirror Move transition: skip ceremony, parchment appears instantly with prompt

Virtue card reveal: all card content instant, no fade

Pulsing ink dots (Foe thinking): replaced with static italic text in margin color: “[Foe name] is composing”

The aesthetic reads quieter under reduced motion. The product remains fully usable.

Repeat-Use Tempo Compression

After the user has completed 5 matches (tracked in localStorage in MVP-0, server-side from V1), default ceremonial pacing compresses automatically.

Specific compressions are listed inline in each motion section above. Summary: match-start ceremony shortens from ~2800ms to ~1200ms; Mirror Move ceremony shortens from ~3000ms to ~1200ms. Every other timing is unchanged.

The mechanic is preserved (parchment rises, prompt fades in, opening claim writes itself); the ceremony scales with familiarity.

User-selectable: under settings (V1+), a “swift” tempo option enables compressed timings from match 1.

Part VI. Surface Treatments

The ten surfaces of the product. Each specifies layout, interaction behavior, accessibility behavior, the element that has to be perfect, and any decision deferred to a later version.

1. Foe Selection (V1+)

MVP-0 has no selection screen; Aristotle is hardcoded. V1 adds this surface.

Layout: Vertical list of Foes, each as a full-width semantic <button> styled as a card. Card contains: Foe name in display serif (large), one-sentence position phrasing in body serif italic in the Foe’s ink accent, tier indicator as typographic mark (•, ••, •••, ••••) in margin color mono. No portraits in V1.

Tier language: Foundational: Legibly Arguable. Demanding: Counterintuitive. Structural: Modern Pressure. Foundation-Shaking: Terms Under Attack. No difficulty numbers.

Interaction: Tap or click anywhere on the card selects the Foe. Cursor pointer on hover; faint hairline underline appears beneath Foe name on hover/focus. Keyboard: Tab through cards, Enter to select.

Accessibility: Each card is a real <button> with aria-label="Choose [Foe name]". Visible focus indicator: 1px functional rule color underline beneath Foe name. Tap target minimum 56px height across full card width.

The element that has to be perfect: The one-line position phrasing for each Foe. This is where Foe selection earns its register. If it sounds like game flavor text, the screen breaks.

Deferred: Locked-Foe treatment (whether locked Foes appear at all, or stay hidden until earned). Recommendation for V1: locked Foes appear muted, with the position line visible but selection disabled.

2. Match Start

First-Match Orientation Screen (MVP-0 only, shown once per user)

Before the first opening claim of a user’s first match ever, a single intro screen displays.

Layout: Empty parchment, centered. Display serif title at 28px: “Argue against Aristotle.” 64px vertical space. Body serif paragraph (16-18px), centered, max-width 480px:

He will defend a position. You will press it. Both of you have HP that depletes when reasoning lands or fails. The match ends when one side breaks or the exchange limit is reached.

64px vertical space. Single text affordance: “Begin.” in italic body serif at 20px, in ink color, semantic <button> styled as text.

Behavior: Tap “Begin.” Intro screen dissolves over 800ms. Standard match-start sequence begins.

Persistence: Stored in localStorage as dc_first_match_complete = true after the first match completes. Never reappears on the same browser/device.

The orientation screen is the only place in MVP-0 with explicit instructional language. The manuscript register holds because the type, color, and spacing are consistent with the rest of the system.

Match Start (every match)

Layout: Empty parchment. Foe’s name in mono small caps top-center. Domain label in italic body serif beneath, in margin color. Initial pause. Foe’s opening claim writes itself in display serif at clamp(22px, 7vw, 26px) on mobile or 32px on desktop, centered, with ceremonial spacing above.

No “Begin Match” button. The product trusts the player to recognize that it is their turn. After the opening claim appears and the input activates, “Your move” placeholder appears in margin-color italic in the input field.

Domain reroll: After the opening claim appears, a single text affordance appears below it: “Reroll claim once.” in mono at 12px in margin color. Disappears after the player either rerolls or submits their first response. Semantic <button> element.

Accessibility: aria-live=“polite” announcement on match start: “Match starting. [Foe name] is preparing to state the opening claim.” After claim appears: aria-live announcement of the claim text itself.

The element that has to be perfect: The pause before the claim arrives. The product is asking the player to enter a serious mode. The pause does that work without announcement.

3. Active Match

Layout: HP rules fixed at top of viewport. Below: metadata row (Foe name in mono, current exchange number, Foe ink accent line). Below: scrollable transcript pane. Below on mobile/tablet: input affordance (tap to open Composition Mode). Below on desktop: input field fixed-bottom.

HP rules: 3px height on mobile/tablet, 2px on desktop. Length depletion is the primary signal: the rule visibly shortens as HP drops, growing toward the center gap. Saturation fade is secondary, applied to the remaining length. At full HP, rule extends across the full half-viewport in full Foe ink (left) or charcoal (right). At 0 HP, rule has shrunk to zero length and zero saturation.

Quality tag placement: - Desktop: right margin, vertically aligned to bottom of player turn. Mono uppercase, +0.04em tracking, 12px, in margin color. No background, no border, no rounded corners. - Mobile/tablet: inline below player turn, 16px gap, same typography.

Input field (desktop): Söhne sans 18-20px. No border. Single hairline rule along the bottom edge (functional rule color #9B8D74 when focused; decorative #C9BFA8 when not). Character counter in lower-right of field, mono 12px in margin color, format “482 / 1000”. Submit on Cmd/Ctrl+Enter or via small italic affordance “Commit response” in lower-right that appears after 30+ characters typed. Disabled with subtle dim during Foe thinking state.

Input area (mobile/tablet): Tap area triggers Composition Mode (Part IV). The visible input area shows placeholder text “Tap to compose your response” in margin-color italic. Character count updates after composer commits.

Foe thinking state: Three slow-pulsing ink dots in the position the Foe’s response will appear. Each dot fades in and out independently, 1800ms cycle, staggered 600ms. In Foe’s ink accent. Calm, not anxious.

Past exchange behavior: One exchange back stays full-fidelity. Two or more exchanges back collapse to spine summary (Part IV).

Accessibility: - HP rules: aria-hidden (the state is announced via match-end summary, not turn-by-turn) - Foe thinking dots: aria-live=“polite” region announcing “[Foe name] is composing a response” - Reduced motion: dots replaced with static italic text “[Foe name] is composing” in margin color - Submit affordance: visible focus state (functional rule color underline at 4px below baseline) - Tab order: input field, submit affordance, transcript scroll region

The element that has to be perfect: The way Foe text and player text sit in the same column without feeling like a chat. The serif/sans contrast plus the alignment difference plus the per-Foe ink accent does this work. If the page reads as Messages or ChatGPT at any point, the visual register has failed.

Deferred: Auto-scroll behavior when new exchange arrives. Recommendation: hold position. Player chooses to read what just happened, not be dragged.

4. Quality Tag Display

Treated extensively in Active Match. Worth restating the discipline.

One tag per turn, single phrase from the 14-tag list

Mono, uppercase, +0.04em letter-spacing, 12px (revised from 13px / +0.08em in v1)

Margin color, no semantic color shift by valence

No background fill, no border, no rounded corner, no icon

No celebration animation, no shake animation

Fade-in 600ms, 200ms after Foe response settles

Persists in spine line when the exchange collapses

The tag is restrained assessment-layer typography in the Rams-discipline register. It is calibrated, modernist marginalia. It is not scribal annotation; the system no longer makes that claim. The discipline of the typography does the entire job. Any drift toward badge styling breaks the register.

5. Match End

Layout: Active match dims to 30% opacity over 1800ms. HP rules complete their final depletion, then dissolve. Single horizontal hairline rule fades in across the column. “The exchange is complete.” in display serif at 20-24px fades in below the rule. 1200ms pause. Mirror Move transition begins.

No outcome announcement. No “YOU WIN.” No “DEFEATED.” No “VICTORY.” The HP state at end-of-match communicates the outcome. The dimming and the rule communicate completion. The product does not announce outcomes; it ends them.

Forfeit treatment: If the player typed /forfeit, the dimming sequence is identical, but the completion text reads “The exchange is withdrawn.” in display serif. Same dignity. Same Mirror Move flow afterward.

Accessibility: aria-live=“assertive” announcement on completion: “The exchange is complete. Outcome: [win/loss/draw]. Mirror Move next.” Reduced motion: instant 30% opacity, instant rule appearance, no fade transitions.

The element that has to be perfect: The absence of celebration. Real philosophical exchanges end with completion, not announcement.

Deferred: Whether the player sees the final HP state for a moment before the bars dissolve. Recommendation: brief 1500ms hold at final state before dissolution. Confirms the outcome is felt.

6. Mirror Move

Layout: Background transitions to deep ink (#0E0B07) over 1800ms (compressed to 800ms after 5 matches). A single block of warm parchment (#F4EDE0) rises into the viewport from below over 1200ms (compressed to 600ms), with a single soft shadow underneath (the only shadow in the product). Display serif prompt fades in 600ms after the parchment settles.

Prompt: “What do you think this match revealed about how you reason under pressure?” Display serif, 24-28px, centered, in ink color (#1A1816 against the parchment surface).

Textarea: Below the prompt with 64px of space between. No border. No background fill. Single faint hairline rule along the bottom edge (functional rule color when focused). Soft cursor. Söhne sans 18-20px in charcoal. The textarea grows as the player types.

Submit affordance: Hidden until 30+ characters typed. When it appears: italic display serif, lower-right of textarea, reading “Submit your reflection.” Semantic <button>. No counter. No “27/30”. No progress indicator.

On submit: Parchment dissolves over 1200ms. Backdrop holds. Virtue reveal sequence begins.

Accessibility: - aria-live=“assertive” on prompt appearance: “Reflection prompt. What did this match reveal about how you reason under pressure?” - Submit affordance: visible focus state (functional rule color underline) - Reduced motion: parchment rises in 400ms; prompt fades in instantly after parchment settles - Cmd/Ctrl+Enter submits

The element that has to be perfect: The prompt typography and the absence of UI chrome. This screen feels like opening a private journal in a still room. Anything that reads as form field breaks it.

Deferred: Whether the player can review the transcript while writing the Mirror Move. Recommendation: a single text affordance “Review transcript” in mono small in the lower-left, opens the transcript in a darkened overlay. Default state is reflection without re-reading.

7. Virtue Profile Reveal Sequence (REVISED IN V2)

This is the largest visual change from v1.

Layout: Mirror Move parchment dissolves; backdrop stays at deep ink. Virtue cards reveal sequentially against this dark backdrop. Each card occupies the full viewport center.

Each card contains, top to bottom:

Dimension name in display serif at 20px (reduced from 28px in v1), in margin-color italic. Reads as label, not headline.

Evidence quote in Tiempos Text Italic at 18-20px in ink color (parchment-tone #E8DFC8 against the dark backdrop), centered, max-width 540px. This is the largest, most visually weighted element on the card.

Score numeral below the evidence quote in mono at 14px in margin color, format “7/10”. No count-up animation. Numeral fades in with the rest of the card content.

Reveal cadence: Each card 600ms total fade-in (revised from 1400ms in v1). Player taps or clicks to advance to next card. No skip-all. No back during sequence. After all cards revealed, brief pause (1200ms), then post-match evidence section fades in beneath the final card.

Card positioning: Single card visible at a time, centered. Previous cards fade behind to 20% opacity at edge of viewport, suggesting depth. Player can tap a faded card to scroll back to it after the sequence completes.

Accessibility: - aria-live=“polite” announcement per card: “Dimension: [name]. Evidence: [quote]. Score: [n] of 10.” - Tab to advance, Enter/Space to advance, arrow keys to navigate forward and back after sequence completes - Reduced motion: all card content instant, no fade

MVP-0: Two cards (Logos, Phronesis). MVP-1 adds Aidōs. V1 adds Sophrosyne, Kairos.

The element that has to be perfect: The visual weight of the evidence quote. The quote is the product. The score is metadata. Visual hierarchy must communicate this without verbal disclaimer.

Why this changed from v1: The 48px count-up numeral was the only counting animation in the product and the largest single element on each virtue card. It made the post-match feel like a high-score reveal regardless of typographic discipline around it. The visual evidence at the climax contradicted the master spec’s “evidence not verdict” thesis. v2 makes the evidence quote the climactic element and demotes the score to metadata. This is genuinely more faithful to the master spec’s framing.

What this is not: A high-score reveal screen. No counting animation. No celebration. No comparison to other players. The score appears as quiet provisional metadata after the evidence has registered. Read the evidence first; see the score second.

8. Strongest Moment, Move You Missed (V1), Development Note (V1)

Layout: After the virtue card sequence completes, post-match evidence appears as a scrollable surface beneath the final virtue card. Backdrop transitions from deep ink back to parchment over 1200ms. Three sections (in V1; MVP-0 has only Strongest Moment) stacked vertically.

Section structure: Mono uppercase label (STRONGEST MOMENT, MOVE YOU MISSED, DEVELOPMENT NOTE) at 13px tracked +0.08em in margin color. Below the label: the content in body serif at reading size (18px), with the relevant transcript quote indented 24px and italicized inline. Quote highlighted with a subtle parchment-tone background (#EDE3CE) extending to the column edges.

Visual weight: These sections occupy more visual real estate than the virtue cards. They sit after the score reveal precisely so they read as the meal, not the dessert. The score is metadata. The evidence is the product.

Accessibility: - Section labels are real <h3> elements styled as mono uppercase - Quotes wrapped in <blockquote> elements - aria-label on each section for screen reader navigation

The element that has to be perfect: The integration of transcript quote into the evidence prose. The reader feels they are seeing the actual moment from the match, not a paraphrase.

MVP-0 architecture: Even with only Strongest Moment, structure as a section with the mono label. The architecture is in place; only the content count differs.

9. Mirror Delta

Layout: After the evidence sections, Mirror Delta appears on its own surface. 168px of vertical space above (responsive on mobile). Single sentence in italic display serif at 20-24px. In ink color, on parchment.

Position in flow: Last thing the player reads before the rematch invitation. Has its own visual breathing room. Not bundled with virtue scores or evidence.

Self-assessment display: The player’s own Mirror Move text appears above the Delta sentence, in body serif italic in margin color, prefixed with mono label “YOU WROTE.” The Delta sentence appears below, prefixed with mono label “THE TRANSCRIPT SUGGESTS.” The gap between the two is visible rather than asserted.

Accessibility: aria-live=“polite” on Mirror Delta appearance. Both sections wrapped in semantic <section> with appropriate aria-label.

The element that has to be perfect: The language. Visual is doing minimal work; the writing carries it. Non-shaming language is non-negotiable. The Delta is observation, not judgment.

Deferred: Whether large Deltas should be tracked across matches as their own pattern. Recommendation: V2, after several matches accumulated.

10. Rematch Invitation (REVISED IN V2)

Layout: Below Mirror Delta, with 104px of vertical space. Two text affordances stacked. Primary: italic body serif at 20px, ink color, reading “Begin again, with a new claim.” Secondary: mono at 12px in margin color, reading “or close this exchange.”

Both are semantic <button> elements with text styling.

Behavior: Single tap on the primary text initiates rematch. A 2-second cancel window appears immediately: the previous post-match content stays visible at 50% opacity, and a small “Cancel rematch” affordance appears in mono at 12px in margin color in the lower-right. After 2 seconds without cancellation, the rematch flow begins (returning to /api/start with a new domain selected).

If the user taps “Cancel rematch” within 2 seconds, the post-match returns to full opacity and the rematch is aborted. No new match state is created.

Single tap on the secondary text closes the post-match flow without confirmation.

Why the cancel window: Rematch is irreversible and accidental taps lose the entire post-match. This is the only confirmation pattern in the product. The rest of the product trusts the player; rematch trusts the player but allows undo.

Accessibility: - Both affordances: cursor pointer, faint underline on hover/focus, visible focus state via functional rule color underline - “Cancel rematch” affordance receives keyboard focus during the 2-second window so Esc or Enter can cancel - Reduced motion: previous content stays at 50% opacity instantly, no transition

V1 addition: When V1 introduces “Rematch with Lesson Applied” feature, this affordance becomes “Begin again with this lesson active” in the same italic body serif. The Development Note from this match remains visible as a small banner at the top of the next match.

The element that has to be perfect: The phrasing. “Begin again,” not “play again.” The product does not think of itself as a game even though it has game mechanics.

Deferred: Whether the player can pivot to a different Foe from this screen. Recommendation: V1 question. MVP-0 has one Foe. V1 adds “Face a different Foe” as a tertiary text affordance.

Part VII. Empty, Loading, and Error States

Empty States

Foe thinking (most-seen state)

Three slow-pulsing ink dots in the position the Foe’s response will appear. Each dot fades in and out independently, 1800ms cycle, staggered 600ms. Color: Foe’s ink accent. No spinner. No “Aristotle is typing” label.

Accessibility: aria-live=“polite” region announcing “[Foe name] is composing a response.” Visually-hidden text in screen reader output. Reduced motion: dots replaced with static italic text in margin color: “[Foe name] is composing.”

Match start before claim arrives

Foe’s name in mono small caps, single horizontal rule beneath. Domain label in italic body serif. Then the initial pause before the opening claim writes itself. The empty page is part of the experience, not a missing state.

Accessibility: aria-live=“polite”: “Match starting. [Foe name] is preparing the opening claim.”

Pre-match (V1+, Foe selection screen reached)

Foe selection list as described in Surface 1. No empty state per se; the selection list is the entry point. If the user has no match history yet, no “welcome” copy. The list itself is the welcome.

Error States

Errors are surfaced without breaking the manuscript register. Even system failures are written in the product’s voice.

JSON parse failure (after retry)

Graceful fallback. The system shows the Foe holding ground generically (“I see you press the point. Let us consider it more carefully.”) and gives the player chip damage rather than 500ing. The error is invisible to the player. The match continues. Server logs the raw response for debugging.

Accessibility: No special announcement needed; the failure is invisible by design.

Network failure

Single line of mono text fades in below the input field: “Connection lost. The exchange will resume.” Match state is preserved server-side. When connection returns, the player picks up where they left off. No modal. No error icon.

Accessibility: aria-live=“assertive”: “Network connection lost. The match state is preserved. The exchange will resume when connection returns.”

Model unavailable

Full-screen state. Single line in display serif at 24px, centered: “The Foe is silent. Please return.” Below it, after 800ms, a small text affordance in italic body serif: “Try again.” No technical jargon. No error code.

Accessibility: aria-live=“assertive”: “The model is currently unavailable. Please try again shortly.” “Try again” affordance receives focus.

Forfeit accepted

Match end sequence runs identically to a normal match end, but completion text reads “The exchange is withdrawn.” Same dignity. Same Mirror Move flow afterward.

Accessibility: aria-live=“polite”: “Forfeit accepted. The exchange is withdrawn. Mirror Move next.”

Validation failure

If the player submits a response that fails server-side validation (extreme length, suspected injection, encoding error), the input area shows: “The system did not accept this response. Try once more.” in margin color italic at 14px below the input. The textarea content is preserved. The submit affordance reactivates.

Accessibility: aria-live=“assertive” on the validation message.

Part VIII. Interaction and Accessibility Rules

This section defines the accessibility floor. Every visual decision must comply.

Semantic HTML

All actionable elements use semantic HTML controls regardless of visual treatment.

<button> for actions (submit, rematch, reroll, advance virtue card, dismiss composer, cancel rematch, begin)

<a href> for navigation (V1+ Foe selection navigation, transcript export download)

<input type="text"> and <textarea> for text input

<form> for the input field with submit handling

<h1>, <h2>, <h3> for headings, styled as needed

<blockquote> for transcript quotes in post-match evidence

<section>, <article> for major surfaces

Visual styling does not change semantic HTML. A button that looks like text is still a <button>.

Focus States

Every interactive element has a visible focus state that meets WCAG 2.4.7. Focus indicator must be:

Visible against parchment background (functional rule color #9B8D74, ~3.0:1 contrast)

Distinct from hover state (focus is keyboard-driven; hover is pointer-driven)

Not solely color-based (line-style change or thickness change required)

Manuscript-native focus treatment:

Text affordances: focus shows a 1px solid underline in functional rule color, 4px below baseline

Input field: focus shows the bottom hairline in functional rule color instead of decorative rule color

Virtue cards (during reveal): focus ring is a 1px hairline rule, 8px outside card bounds, in functional rule color

Foe selection cards (V1+): focus shows underline beneath Foe name in functional rule color

Hover treatment (pointer-driven): cursor pointer plus faint underline (1px decorative rule color) appearing at 4px below baseline. Distinct from focus state.

Keyboard Navigation

Full keyboard navigation across all surfaces. Tab order matches reading order. No keyboard traps. Escape dismisses any overlay (Mirror Move cannot be dismissed mid-write, but composition mode can be cancelled, and rematch cancel window responds to Esc).

Submit on the input field: Cmd/Ctrl+Enter or Enter (if textarea is single-paragraph). Shift+Enter for newline within textarea. Submit on Mirror Move: Cmd/Ctrl+Enter only.

Virtue card sequence: Tab or Enter to advance. Arrow keys to navigate after sequence completes.

Tap Targets

Minimum 44x44px tap target on touch devices for all interactive elements. Text affordances (“Begin again”, “Commit response”, “Cancel rematch”, “Begin”, “Try again”) have invisible padding extending tap area to 44px height even when visual element is smaller.

Foe selection cards (V1+): minimum 56px height across full card width.

ARIA Live Regions

Three live regions in the document:

role="status" aria-live="polite" for non-urgent updates: Foe thinking, match started, terrain shifted

role="alert" aria-live="assertive" for urgent updates: Mirror Move prompt, match end completion, network failure, model unavailable, validation failure

role="log" aria-live="polite" on transcript: each new exchange appends to log

Visual elements that hide labels (pulsing ink dots, terrain shift marker) include visually-hidden text in live regions for screen readers.

Reduced Motion

prefers-reduced-motion: reduce triggers global motion overrides as defined in Part V. All ceremonial transitions collapse to instant or 150ms minimum. The aesthetic reads quieter; the product remains fully usable.

Contrast Thresholds

WCAG AA minimum (4.5:1 for body text, 3:1 for large text >=24px) enforced for all text/background combinations. WCAG AAA preferred where the readable register permits.

Functional UI elements (input boundaries, focus indicators, active rule color) must reach 3:1 contrast against parchment background per WCAG 2.4.7. Decorative elements (transcript dividers, hairline ornament) may go below 3:1.

Foe accent ink at sizes below 16px is forbidden. The collapsed transcript spine at 14px sits in margin color throughout.

Browser Zoom

The product must function without layout breaking up to 200% browser zoom. No fixed-px containers preventing text-only enlargement. Layout reflows; text grows; content remains accessible.

Low-Vision and Dyslexia Considerations

Generous line-height (1.6 to 1.7) on all body text

Adequate paragraph spacing (md = 24px)

Left-aligned body text only; never justified (justification creates uneven word spacing harmful to dyslexic readers)

Sufficient contrast at body size for AA pass minimum

Critical actions never set in mono uppercase only; mono is metadata register, not primary action register

All text remains in normal/medium weight range; no thin weights below 400

V2 will add a high-contrast mode and an optional sans-serif body face for users who find serif fatiguing. MVP-0 ships with a single canonical reading mode; the floor is WCAG AA, not personalization.

Part IX. Iconography, Sound, and Export

Iconography

The product has no iconographic system. No SVG icons. No icon fonts. No emoji. The only graphic elements are typographic ornaments: the em-dash separator in select labels, hairline rules at section boundaries, and the typographic tier marks (•, ••, •••, ••••) on Foe selection cards.

This is non-negotiable. Adding a single icon anywhere pulls the system toward modern app aesthetic.

Sound

No sound in MVP-0 or V1. V2 considers sound design with paper-and-ink vocabulary only (rustle, settle, scratch). Never tones. Never pings. Never button-press sounds. Sound design will receive its own dedicated design pass when V2 begins.

Print and PDF Export Direction (V1)

V1’s transcript export feature requires a dedicated design pass before implementation. The “manuscript register preserved” claim has no print specification in MVP-0. V1 print spec will address:

Print-specific type sizing (8 to 10pt body, 14pt display)

CMYK ink color translation (warm browns will print muddy in standard CMYK; consider single-ink black with typographic register for print)

Page margins and column structure for letter-size and A4

Header and footer treatment (match metadata, page numbers, date)

HP rules removed in print (state is past, not active)

Transcript with Foe and Player typographic distinction preserved

Quality tags as actual margin notes

Post-match evidence sections after transcript

V1 print is deferred to its own design document. MVP-0 has no export.

Source Languages and Internationalization

MVP-0 and V1 are English-only across all dialogue, claims, evidence quotes, and post-match output. No source-language quotes from Aristotle (Greek), Confucius or Mencius (Classical Chinese), Ibn Rushd (Arabic), or any other non-Anglophone Foe. The roster includes non-Western thinkers in V1; the dialogue remains in English.

This is stated explicitly to prevent ambiguity. A scholarly user expecting to see Greek or Arabic source-text quotation will not see it in MVP-0 or V1.

V2 addresses multi-script typesetting:

Noto Serif and Noto Sans for primary Latin

Noto Serif Greek, Noto Serif CJK SC and TC, Noto Naskh Arabic for source-language quotation

Defined typographic relationship between primary and source-language faces (matched x-height, paired weights)

Right-to-left support for Arabic

Vertical text consideration for Classical Chinese (likely deferred further)

V2 source-language treatment will be specified in its own design pass.

Part X. Implementation Discipline

Drift Risks

The aesthetic system is opinionated and will erode under casual modification. Common drift directions to defend against:

Modern app density. Pulling the layout tighter to fit more on screen. The product is generous by design; do not compress spacing.

Friendly button styling. There are no conventional buttons. Submit affordances, rematch affordances, reroll affordances are semantic <button> elements styled as text. Adding fill, border, or rounded corners reads as “game.”

Colored toasts and notifications. The product has no toast system. Quality tags are not toasts. Errors are not toasts.

Loading spinners. No CSS spinners. No animated SVG loaders. The Foe thinking state is three slow ink dots and nothing else. Empty states are empty parchment.

Modal dialogs. No confirmation dialogs except the rematch cancel window. No “are you sure” modals.

Accent color creep. The Foe’s ink accent is only used as the color of that Foe’s text. Not for buttons, links, borders, accents, hover states, or backgrounds.

Saturated colors. The palette is warm and desaturated. Any saturated color reads as discordant.

Visual purity at the cost of accessibility. Hiding affordances, removing focus states, or using mono uppercase for actionable elements degrades the product. Restraint serves the user, not the metaphor.

Game vocabulary creeping back. Score animations, comparison features, leaderboards, achievements, level indicators. The visual system commits against game language; engineers will sometimes propose adding it for “engagement.” Reject.

Quality Gate Checklist

Before any visual element ships, it passes through these questions:

Does it look like a printed page or a screen pretending to be paper?

Would this element appear in a serious contemporary edition of an old text?

Does it use color to communicate, or only to set register?

Does it announce itself, or quietly do its work?

Does it move only where motion carries meaning?

Does it trust the player while remaining usable to them?

Is it operable via keyboard? Does it announce its state to a screen reader?

Does it work at 200% browser zoom without breaking layout?

Does it meet WCAG AA contrast at the size it ships?

If any answer is wrong, the element gets cut or redesigned. Not compromised.

What Developers May Adjust Without Design Approval

Accessibility-required adjustments do not require design review if they preserve the visual register:

Adding ARIA attributes

Adding visually-hidden text for screen readers

Adjusting tap target invisible padding

Adding focus indicators that meet WCAG 2.4.7

Switching <div> to <button> or other semantic element for actionable elements

Adding prefers-reduced-motion overrides

Adjusting font-display or font-loading behavior for performance

Adding aria-label and aria-describedby for clarity

Visual-aesthetic adjustments require design approval:

Color changes

Type face or size changes

Spacing changes

Motion timing or curve changes

New surface treatments

New affordances or state indicators

Part XI. Versioning Roadmap

The aesthetic direction is locked at v2. Implementation fidelity ships in stages. Restraint is the feature. The visual system at MVP-0 is complete in its core elements; later versions extend rather than repair.

MVP-0

Full type stack with three-tier font fallback (canonical Klim, free production-safe, system)

Full type scale across mobile, tablet, desktop

Light parchment color system with Aristotle’s amber-brown as the only Foe ink

Functional and decorative rule color split

Spacing scale and three-breakpoint layout grid (mobile, tablet, desktop)

Mobile composition mode for input

Full motion vocabulary with reduced-motion overrides

Repeat-use tempo compression after 5 matches

All ten surface treatments at functional fidelity

Virtue card reveal: evidence-led, score as metadata, no count-up

Foe response: full-statement fade-in, no token streaming

HP depletion: length plus saturation

Empty states (Foe thinking, match start, model unavailable)

Error states (parse failure fallback, network failure, validation failure, forfeit)

First-match orientation screen

Misclick protection on rematch (2-second cancel window)

Iconography rule (none, with em-dash exception)

Full Part VIII accessibility compliance

Drift discipline checklist enforced in code review

Match log to server console as JSON

MVP-1 (with Machiavelli)

Add Machiavelli’s per-Foe ink accent (#2B2D3A iron-gall blue-black)

Foe selection screen at match start (Aristotle vs Machiavelli)

Aidōs virtue card added to reveal sequence (3 cards instead of 2)

Argument Map section in post-match output

V1

Per-Foe ink palette across all 8 V1 Foes

Move You Missed and Development Note sections in post-match

Rematch with Lesson Applied: Development Note persists as banner in next match

Replay highlights (2 to 4 transcript moments flagged)

Transcript export styling (dedicated design pass for print and PDF)

Foe portraits considered (only if commissioned in single coherent stippled engraving style; otherwise deferred to V2)

Refined motion timing based on real player observation from MVP-0 sessions

User-selectable swift tempo mode in settings

“Face a different Foe” affordance on rematch screen

Concede button as explicit UI alternative to /forfeit command

V2+

Hexis indicator dashboard (own visual language; cross-match pattern data may need a treatment closer to brutalist/archival than the manuscript register; dedicated design pass)

Dark mode setting (warm-parchment-becomes-deep-paper logic, never pure-dark UI inversion)

Sound design (paper-and-ink vocabulary only)

Foe portraits if commissioned

Council of Models disagreement display

Multi-script typesetting (Greek, Chinese, Arabic) with Noto-family fallbacks

High-contrast accessibility mode

Optional sans-serif body face for users who find serif fatiguing

Tracked Mirror Delta patterns across matches

Permanently Held

Animations beyond the quiet vocabulary

Iconographic system (icons remain forbidden)

Color use beyond ink-and-parchment palette

Avatars in any non-engraving style

Decorative ornaments, illustrative flourishes, drop caps

Anything that would make the product look like a game rather than a serious text

Score numeral count-up animation

Token streaming of Foe responses

Modal confirmation dialogs (except rematch cancel window)

Toast notifications

Final Note

The product looks like a serious contemporary edition of a serious old text. Not a re-enactment. An inheritance.

Aristotle does not speak in Helvetica. He speaks in Tiempos. The reader writes back in their own contemporary hand against an old text in its own historical ink.

The visual system carries the philosophical claim. Combat is the surface. Phronesis is the engine. Type, space, and restraint do most of the work.

The Mirror Move is the soul. The evidence quote in the post-match is the system’s verdict on the match. The score is metadata. The transcript is the artifact.

Everything else serves these.

Visual Design System v2. Final MVP-0 build spec. Companion to Master Spec v2.
