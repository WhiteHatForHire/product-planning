---
title: "ANCHOR — EXPO MOBILE CONVERSION GUIDE"
source_archive: "Symposium Studios"
source_path: "######Symposium Studios/# Products /Anchor Sobriety/ANCHOR — EXPO MOBILE CONVERSION GUIDE.docx"
status: active
privacy: working
tags:
  - product
---

# ANCHOR — EXPO MOBILE CONVERSION GUIDE

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
ANCHOR — EXPO MOBILE CONVERSION GUIDE

For Replit — Step by Step

Written for a systems thinker, not a framework specialist

What You’re Doing and Why

You have a working web app running on Node.js/Express with a plain HTML frontend. You’re going to fork that project in Replit, keep the entire backend exactly as-is, and replace the frontend with a React Native/Expo mobile app.

The Backend: (server.js, database, all API routes, OpenAI calls) stays untouched.

The Frontend: (all HTML, CSS, JS files) gets replaced with React Native screens.

Development: Your phone connects to the Replit project through Expo Go.

Production: When ready, EAS Build produces an .ipa file you upload to TestFlight.

Think of it like this: the engine stays the same. You’re putting a new body on the car.

Prerequisites — Do These First

Apple Developer account: Ensure it is active (check developer.apple.com).

V2D Complete: Your web app must be working correctly.

Expo Go App: Installed on your iPhone.

Expo.dev Account: Sign up at expo.dev.

Phase 1: Fork the Project in Replit

Open your existing Anchor project in Replit.

Click the project name at the top left.

Look for “Fork” or “Duplicate” in the menu.

Name the new project “Anchor Mobile” or “Anchor iOS”.

Replit creates an identical copy — your original is untouched.

Phase 2: Project Architecture

Understand the isolation between the server and the mobile client.

Category

Staying (Backend)

Going (Frontend)

Logic

server.js, API routes, OpenAI integration

/public folder, HTML/CSS files

Data

DB connection, SQL queries

Static web JS files

Env

Replit Secrets (.env)

N/A

Phase 3: Replit Agent Conversion Prompt

Copy and paste this entire prompt into Replit Agent to initialize the /mobile directory:

Convert this existing Node.js/Express recovery check-in app into a hybrid project that runs both the existing Express backend AND a new React Native/Expo mobile frontend.

CRITICAL CONSTRAINTS:
- Do NOT modify server.js or any backend API routes
- Do NOT modify the database connection or any SQL queries
- Do NOT remove or modify any existing npm backend packages
- Do NOT touch any Replit Secrets or environment variables
- The Express backend must continue to run exactly as it does now
- Only add new files and a new /mobile directory for the Expo app

PROJECT STRUCTURE:
- Keep all existing backend files exactly as-is
- Create a new /mobile directory containing the entire Expo app

EXPO SETUP:
- Initialize project inside /mobile: npx create-expo-app mobile --template blank
- Use React Native with Expo SDK, Expo Router for navigation, and NativeWind for styling.
- Target iOS first.

NAVIGATION:
Set up five bottom tabs using Expo Router: Home, Check In, History, Trackers, Insights.

SCREENS TO BUILD:
1. Home: Header with date, sobriety cards (GET /api/trackers), and latest check-in summary.
2. Check In: Full/Quick modes with 1-10 sliders, pill toggles for habits, and trigger tags. POST to /api/checkin.
3. History: List view from GET /api/history with tap-to-detail.
4. Trackers: Active list with live duration counters. Add/Reset tracker flows.
5. Insights: Stats cards, line charts (react-native-chart-kit), and calendar heatmap.

DESIGN:
- Dark theme (#0D0D0D), white primary text, muted green accent (#4DB6AC).
- Cards with subtle border radius. Standard iOS System fonts.

Phase 4: Local Development Loop

Navigate to the folder: cd mobile

Start the server: npx expo start

Open Expo Go on your iPhone and scan the QR code.

Hot Reload: Saving any file in Replit will update the app on your phone in seconds.

Phase 5: Build for TestFlight

Install CLI: npm install -g eas-cli

Login: eas login

Configure: eas build:configure (Choose iOS)

Build: eas build --platform ios

Upload the resulting .ipa file via Transporter (Mac) or App Store Connect.

Common Issues and Fixes

Metro Bundler Error: Run cd mobile && npm install.

API Calls Failing: Verify API_BASE matches your Replit preview URL.

EAS Build Fails: Check logs on expo.dev; usually a bundle identifier mismatch.
