---
title: "Project 1 The Living Landing Page"
source_archive: "Software Projects"
source_path: "####Software Projects/2 - Project planning/Project 1_ The Living Landing Page.docx"
status: reference
privacy: private/internal
tags:
  - product
---

# Project 1 The Living Landing Page

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Project 1: The Living Landing Page. This is a one-day build if you stay locked in.

The Build: Living Landing Page

Stack: Next.js + Tailwind CSS + Framer Motion, deployed on Vercel with a custom domain.

Sections: Hero, Features, Testimonials, FAQ, Pricing, CTA, Contact Form, Mobile Nav, Dark Mode.

Done condition: Live URL, loads under 1 second globally, your name on it.

Hour-by-Hour Execution

Hour 0–0.5: Decide What Product This Is For

This is the most important 30 minutes. Don’t build a generic landing page — pick a product you’d actually want to ship. Given where you’re headed, strong options:

∙	An AI-powered tool you’ll build in Project 4 (cold email generator, document analyzer, resume reviewer)

∙	A productized service page for your fCTO offering

∙	A micro-SaaS concept you’ve been kicking around

Write the one-sentence product premise, then sketch the page sections on paper or in notes. Who’s it for, what’s the headline, what are 3-4 features, what’s the pricing.

Hour 0.5–1: Scaffold

npx create-next-app@latest project-1 --typescript --tailwind --app --eslint

cd project-1

npm install framer-motion

npm install lucide-react  # icons

git init && git add . && git commit -m "chore: initial scaffold"

Create your GitHub repo, push it up. Connect it to Vercel right now — you want deploys working from minute one so you can see progress live.

gh repo create project-1 --private --push

Then go to vercel.com → Import → select the repo → deploy. You now have a live preview URL.

Hour 1–2: Build the Layout Shell + Dark Mode

In app/layout.tsx, set up your dark mode toggle (class-based with Tailwind’s darkMode: 'class'). Build your Navbar component with mobile hamburger menu. Build your Footer.

Use v0.dev here — prompt it: “Next.js landing page navbar with logo, nav links, dark mode toggle, and mobile hamburger menu using Tailwind CSS and Framer Motion for the mobile menu animation.”

Copy the output, refine in Cursor, move on. Don’t spend more than 30 min on nav.

Hour 2–3.5: Hero + Features + CTA Sections

Build each as its own component in /components:

∙	Hero: Big headline, subhead, CTA button, maybe a product screenshot/mockup. Framer Motion fade-in on load.

∙	Features: 3-4 feature cards in a grid. Icons from Lucide. Short punchy copy.

∙	CTA: Simple “Get Started” or “Join Waitlist” section between major blocks.

Use v0.dev to generate the initial layout for each, then customize. The key Framer Motion patterns you’ll use:

import { motion } from "framer-motion"

<motion.div

initial={{ opacity: 0, y: 20 }}

whileInView={{ opacity: 1, y: 0 }}

transition={{ duration: 0.5 }}

viewport={{ once: true }}

>

{/* content */}

</motion.div>

Hour 3.5–4.5: Testimonials + Pricing + FAQ

∙	Testimonials: 3 cards with photo placeholder, name, quote. Fake data is fine — this is a portfolio piece proving you can build the section.

∙	Pricing: 2-3 tier cards (Free / Pro / Enterprise pattern). Highlight the middle tier. Use a subtle Framer Motion hover scale.

∙	FAQ: Accordion component. Framer Motion AnimatePresence for expand/collapse.

Hour 4.5–5: Contact Form

Build a working contact form. For today, you have two options:

∙	Quick: Use Formspree or Resend to actually receive submissions (no backend needed)

∙	Quicker: Wire up a form that validates client-side and shows a success toast — you can hook up the backend later

Form fields: Name, Email, Message. Client-side validation. Success state with Framer Motion.

Hour 5–5.5: Responsive QA + Polish

Open Chrome DevTools → toggle every breakpoint. Check:

∙	Mobile nav works (hamburger opens/closes)

∙	All sections stack properly on mobile

∙	Text is readable at every size

∙	Dark mode looks good on every section

∙	No horizontal scroll anywhere

∙	Framer Motion animations aren’t janky on mobile (use viewport={{ once: true }} to prevent re-triggering)

Hour 5.5–6: Custom Domain + Final Deploy

1.	Buy a domain if you don’t have one (Namecheap or Cloudflare Registrar)

2.	In Vercel → Settings → Domains → Add your domain

3.	Update DNS records (Vercel gives you the exact records)

4.	Push final code, let Vercel build

5.	SSL is automatic

Run a Lighthouse audit — target Performance > 90, Accessibility > 90.

Hour 6–6.5: Documentation

∙	Write the README: what it is, stack used, architecture decisions, how to run locally

∙	Write 1-2 ADRs (e.g., “Why Next.js App Router over Pages Router”, “Why Framer Motion over CSS animations”)

∙	Take 3-5 screenshots for your portfolio

∙	Record a 2-min Loom walkthrough

Gate Check (from your playbook)

You’re done when:

∙	Live URL with your name on it ✅

∙	Loads under 1 second globally ✅

∙	Hero, features, testimonials, FAQ, pricing, CTA, contact form, mobile nav, dark mode — all present ✅

∙	README with ADRs ✅

∙	git push → build → CDN → URL pipeline proven ✅

The Trap to Avoid

The Polish Trap (Anti-Pattern #4 from your playbook). You will be tempted to spend 2 hours on gradient tweaks, font pairings, or a parallax effect nobody asked for. Use v0.dev to generate, refine quickly in Cursor, and ship. This is Project 1 of 15 — velocity is the point.

Go build it. 🔨​​​​​​​​​​​​​​​​
