---
title: "Vite Quick Guide for VS Code"
source_archive: "Software Projects"
source_path: "####Software Projects/1 - References/Vite Quick Guide for VS Code.docx"
status: active
privacy: working
tags:
  - planning
---

# Vite Quick Guide for VS Code

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Vite Quick Guide for VS Code

What Vite is

Vite is a fast front-end dev server and build tool. It works very well with React and is a common way to start modern front-end projects. Vite’s official docs say current versions require Node.js 20.19+ or 22.12+. (vitejs)

1. Check Node is installed

In terminal:

node --version

npm --version

If Node is missing or old, update it first. Vite currently requires Node.js 20.19+ or 22.12+. (vitejs)

2. Create a new Vite project

From terminal in VS Code:

npm create vite@latest

Vite’s official getting started guide uses this command to scaffold a new project. (vitejs)

It will ask you:

project name

framework

variant

For React, choose:

React

JavaScript or TypeScript

3. Enter the project folder

cd your-project-name

4. Install dependencies

npm install

5. Start the local dev server

npm run dev

Vite will start a local development server for previewing your app while you work. (vitejs)

6. Open it in your browser

Usually Vite shows a local URL like:

http://localhost:5173

Open that in your browser to preview the app.

7. Main workflow in VS Code

Your normal loop is:

npm run dev

Then:

edit files in VS Code

save

see changes refresh quickly in browser

Vite supports fast hot updates during development, including React Fast Refresh support. (vitejs)

8. Build for production later

When you want a production build:

npm run build

Vite’s build guide says this runs vite build and creates a production-ready bundle. (vitejs)

9. Preview the production build locally

npm run preview

That lets you check the built version before deploying.

Fast React version

npm create vite@latest my-app

cd my-app

npm install

npm run dev

Choose:

React

JavaScript

Good folder pairing with GitHub

After creating the project:

git init

git add .

git commit -m "Initial Vite setup"

gh repo create my-app --public --source . --push

Best use case

Use Vite when you want:

a modern front-end app

React support

fast local preview

an easy path beyond plain HTML files

If you want, I can turn this into a matching VITE_GUIDE.md in the same style as your Git guide.

That error is straightforward:

npm run dev only works in a folder that has a package.json file.

Your current folder is just a basic Git project with index.html, not a Vite/npm app yet. So npm is saying: “I don’t see a package.json, so I have nothing to run.”

What this means

Right now you likely have:

a plain HTML project

GitHub connected

no Vite project created yet

So npm run dev is the wrong command for this specific folder.

What to do instead

If this is just a plain HTML/CSS/JS project

Use Live Server in VS Code.

Steps:

Open Extensions

Install Live Server

Open index.html

Click Go Live

That’s the right preview method for this current project.

If you want this folder to become a Vite app

Then you need to create a Vite project structure first.

From terminal, go up one level if needed, then run:

npm create vite@latest

Choose:

project name

React or Vanilla

JavaScript or TypeScript

Then:

cd your-project-name

npm install

npm run dev

That will work because Vite creates the package.json.

Quick rule

Plain index.html project → use Live Server

Vite project → use npm install and npm run dev

How to check which kind of project you’re in

Run:

dir

If you do not see package.json, then it is not an npm/Vite app.

If you do see package.json, then npm run dev should work.

Best move right now

For the project in your screenshot, use Live Server.

Then when you want your first proper React/Vite app, make a new project with:

npm create vite@latest my-app

cd my-app

npm install

npm run dev

If you want, I can give you a very simple “when to use Live Server vs Vite” cheat sheet next.
