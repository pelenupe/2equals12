# DESIGN.md

## Overview
2 Equals 12 is a full-stack Flask web application designed to celebrate and explore Black history facts daily. The site offers a rotating daily fact, predictive search for topics, AI-powered exploration via OpenAI, an organized topics list grouped alphabetically, and inspirational quotes.

The project is deployed and running live at:
[https://app.2equals12.com](https://app.2equals12.com)

Available on the Apple App Store:
[https://apps.apple.com/us/app/2equals12/id6745202800](https://apps.apple.com/us/app/2equals12/id6745202800)

Available on Google Play Store:
[https://play.google.com/store/apps/details?id=com.blactive.twoequalstwelve&pli=1](https://play.google.com/store/apps/details?id=com.blactive.twoequalstwelve&pli=1)

## The primary goals of the project were:

Create an easy-to-navigate experience around pre-populated historical black history facts.

Allow users to search and explore topics dynamically for more information.

Integrate an OpenAI-powered exploration engine, which will return search results from a black history perspective.

Optimize for mobile experiences (with desktop available too, but not the focus).

## Architecture
Frontend: HTML5, TailwindCSS (via CDN), Vanilla JavaScript

Backend: Python 3 with Flask

Database: SQLite (facts.db)

APIs: OpenAI API for generating exploration responses

Deployment: Linux server (gunicorn + nginx)

## Implementation Details
Flask Application (app.py):
The Flask app is structured around routes like /, /topics, /quotes, /about, and /explore/<tag>. Utility functions like get_fact_by_date() and get_all_categories_and_tags() pull content dynamically from the database.

### Database (facts.db):
The SQLite database contains two tables:

facts: stores facts with fields for date, fact text, category, and tags.

quotes: stores inspirational quotes tied to each month.

#### Schema:

CREATE TABLE IF NOT EXISTS facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    fact TEXT NOT NULL,
    category TEXT NOT NULL,
    tags TEXT
);

CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT NOT NULL,
    quote TEXT NOT NULL,
    author TEXT NOT NULL
);
### Splash Screen:
Users will see a splash screen with the 2 Equals 12 logo before the page loads

### Predictive Search:
Every page features a top navigation search icon that toggles a dropdown predictive search bar.
When the user clicks the search icon, a text input appears.
As the user types, matching tags from the allTags JavaScript array (passed from Flask via Jinja) are dynamically suggested.
Selecting a suggestion or pressing Enter triggers a redirect to /explore/<topic>.
Preloader animation appears while navigating to simulate smooth transitions.

#### Design Decisions (Predictive Search):

Implemented globally inside layout.html, so it's available across every page.
Tailwind utility classes like hover:bg-green-400 and text-black are used for quick style changes.
Designed mobile-first: input fields and hit areas are touch-friendly and sized for smartphones.

### Topics Page (/topics):
Displays all tags sorted alphabetically into four collapsible accordion sections: A–F, G–L, M–R, S–Z.
Grouping topics improves usability on mobile screens instead of showing hundreds of links in one giant scroll.

#### Accordion Mechanism:

Built manually with lightweight JavaScript (toggleAccordion(id)).
No third-party JS libraries (like Bootstrap or AlpineJS) are used.

##### OpenAI Explore Feature (/explore/<tag>):
When a user selects a tag or submits a search, the app uses OpenAI’s API (via ai.py) to dynamically generate an exploration article about the selected topic.

Content is educational, factual, and generated on the fly.

Streaming is simulated to enhance UX.

Potential for caching exists to save repeated calls.

### Preloader Logic:
Clicking a search suggestion or navigation link shows a simple animated spinner overlay (#preloader) until the next page fully loads.

### Progressive Web App (PWA) Support

To improve mobile experience and give users an option to “install” the site, 2 Equals 12 includes PWA capabilities:

- **Manifest File** (`manifest.json`) defines app name, icons, theme color, and start URL.
- **Service Worker** (`service-worker.js`) caches core assets to allow basic offline access.
- **Install Prompt (Android)**: A custom logic could be added to trigger an install prompt for Android users who have not installed the app.
- **No Banner on iOS**: To avoid redundancy, no PWA install banner is shown on iOS. Instead, iOS users are directed to the App Store.

#### Design Decision:
PWA features were added to enhance the experience on Android and for users who prefer lightweight installation. However, the primary delivery method remains the native app stores, where a more integrated experience is possible.


### Challenges Encountered
Predictive Search Conflicts:
Early problems arose with duplicated search bars and IDs when trying to support multiple predictive searches (main layout and topics page). Final solution: move all predictive search logic to the navigation dropdown only.

#### Mobile Compatibility:
Adjustments were necessary to ensure safe-area insets (like iPhone notches and bottom home indicators) were respected.
Added padding-bottom to the mobile nav bar to prevent overlap issues.

#### Preloader Timing:
Flickers were initially common when moving between pages. Event listeners were adjusted carefully to avoid displaying the loader after instant loads.

### Future Improvements
Caching OpenAI exploration results for faster repeated queries.

Creating a newsletter to send out daily facts and/or a push notification.

Adding "favorites" or "saved facts" via localStorage or user accounts.

Enhancing accessibility (keyboard navigation, ARIA labels).

Exposing a full REST API for third-party apps to pull facts and quotes.

## Conclusion
This project was built from scratch with an emphasis on speed, simplicity, and mobile-first design.
By leveraging Flask, SQLite, OpenAI, and TailwindCSS, 2 Equals 12 creates an engaging educational platform with minimal technical overhead.

Dynamic OpenAI exploration means the platform evolves over time without requiring static content updates.

