# 2 Equals 12

2 Equals 12 is a daily Black History fact web application built with Flask. It presents a new fact each day and allows users to explore topics in Black history through predictive search and AI-powered exploration.

## Features

- 📅 **Daily Fact**: Each calendar day reveals a unique historical fact from Black history.
- 🔍 **Predictive Dropdown Search**: A site-wide search icon in the top navigation toggles a predictive dropdown input.
- 🤖 **OpenAI Integration**: Selecting a topic dynamically loads an AI-generated exploration of the subject using the OpenAI API.
- 📚 **Accordion Topics Page**: The `/topics` route groups all tags into four collapsible ranges (A–F, G–L, M–R, S–Z) for easy browsing.
- ✨ **Preloader Animation**: Smooth page transitions are enhanced with a custom preloader spinner.
- 📱 **Mobile-First Design**: Optimized for mobile users, including safe-area handling for iOS devices.
- 🎨 **Custom Styling**: Styled using TailwindCSS with Monoton and Oswald Google Fonts.

---

## 🧠 OpenAI Explore

- Every topic links to a custom prompt sent to OpenAI.
- The AI returns a fact-based, educational paragraph exploring the topic in detail.
- Results are streamed live into the `/explore/<tag>` page for a dynamic experience.

---

## 📦 Progressive Web App (PWA)

- **Manifest**: A `manifest.json` defines app icons, name, theme, and startup behavior.
- **Service Worker**: A `service-worker.js` caches core files for offline access.
- **Android Users**: Will receive a prompt to install the app to their home screen.
- **iOS Users**: Encouraged to install the full native app from the App Store (no auto PWA banner on iOS).

## App Stores

  - ✅ [iOS App Store](https://apps.apple.com/us/app/2equals12/id6745202800)
  - ✅ [Google Play Store](https://play.google.com/store/apps/details?id=com.blactive.twoequalstwelve) 

---

## 🔗 Live Demo

👉 [Visit the live app](https://app.2equals12.com)

---

## ⚙️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/pelenupe/2equals12.git
   cd 2equals12
2. Set up a Python virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Initialize the database:
   sqlite3 facts.db < schema.sql
5. Add your OpenAI API key to .env:
   Obtain API key from: [https://auth.openai.com/](https://auth.openai.com/)
   OPENAI_API_KEY=your_key_here
6. To Run in a development environment:
   Run:
   export OPENAI_API_KEY=your_key_here
   python app.py