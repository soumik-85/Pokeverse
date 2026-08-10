# 🎮 PokeVerse

### A Pokémon Encyclopedia & Interactive Web Experience

🌐 **Live Website:** https://pokeverse-lgf.onrender.com

PokeVerse is a full-stack Pokémon web application designed to provide an interactive and organized way to explore Pokémon, their types, evolutions, games, historical milestones, and quizzes.

What started as a Pokémon website project gradually evolved into a complete web application with external API integration, a custom SQLite database, interactive JavaScript features, responsive UI design, Git/GitHub version control, and live cloud deployment.

---

## 🌐 Live Demo

🔗 **Visit PokeVerse:**  
https://pokeverse-lgf.onrender.com

> For the best experience, PokeVerse is recommended on a laptop or desktop. If viewing from a mobile device, enable **Desktop Site** in your browser.

---

## ✨ Features

### 🔴 Pokémon Hub

The Pokémon Hub provides a centralized place to explore Pokémon and access the main Pokémon-related features of PokeVerse.

- National Pokédex
- Pokémon search
- Pokémon details
- Types
- Abilities
- Base statistics
- Evolution information
- Pokémon artwork and information from PokéAPI

### 🔍 National Pokédex

The National Pokédex allows users to browse and search Pokémon.

Features include:

- Pokémon listing
- Pagination
- Search functionality
- Individual Pokémon selection
- Detailed Pokémon information

### ⚡ Type Explorer

The Type Explorer allows users to explore different Pokémon types.

Users can explore:

- Type names
- Type descriptions
- Type characteristics
- Featured Pokémon
- Type effectiveness

### 🧬 Evolution Explorer

Users can explore Pokémon evolution chains, including:

- Evolution stages
- Previous and next evolutions
- Evolution relationships
- Pokémon artwork
- Evolution information

### 📊 Type Effectiveness

PokeVerse includes a Type Effectiveness system that helps users understand how Pokémon types interact.

It covers:

- Super effective
- Not very effective
- Normal effectiveness
- Immunities

---

# 🧠 Pokémon Quiz Center

PokeVerse includes a dedicated Quiz Center with multiple quiz modes.

### Quiz Modes

- 🎯 Who's That Pokémon
- ⚡ Type Quiz
- 🔄 Evolution Quiz
- 🧠 Pokémon Trivia

The project also includes a Pokémon Master Challenge that combines different question types.

### Quiz Features

- Randomized questions
- Multiple-choice answers
- Score tracking
- Correct/wrong answer feedback
- Interactive question navigation
- Final results
- Session-based quiz state

---

# 🎮 Pokémon Games Encyclopedia

The Games section is designed to feel like a Pokémon game encyclopedia rather than simply displaying a list of games.

It organizes Pokémon main-series games by generation.

Game information can include:

- Game title
- Generation
- Region
- Release dates
- Platform
- Developer
- Publisher
- Average play time
- Difficulty
- Overview
- Key features
- Starter Pokémon
- Legendary Pokémon
- Gym Leaders
- Elite Four
- Champion
- Related games

The Games system uses a custom SQLite database to store structured information.

---

# 📜 Pokémon Timeline

PokeVerse includes an interactive Pokémon historical timeline covering important events throughout the franchise.

Users can:

- Browse events chronologically
- Select individual events
- View event details
- View event categories
- View event images
- Navigate between historical milestones

The timeline uses a two-panel layout with timeline events on one side and detailed event information on the other.

The selected event is highlighted and the detail panel updates dynamically.

The timeline also includes directional slide animations when navigating between events.

---

# 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Backend

- Python
- Flask

### Database

- SQLite

### External API

- PokéAPI

### Production Server

- Gunicorn

### Hosting

- Render

### Version Control

- Git
- GitHub

---

# 🔌 PokéAPI Integration

PokeVerse uses PokéAPI as the primary external source for Pokémon-related information.

PokéAPI provides structured Pokémon data through REST API endpoints.

The Flask backend communicates with the API using Python's `requests` library.

### Data Flow

```text
User
  ↓
Flask Route
  ↓
Python requests
  ↓
PokéAPI
  ↓
JSON Response
  ↓
Flask Processing
  ↓
Jinja Template
  ↓
User Interface

Using PokéAPI allows PokeVerse to retrieve Pokémon information dynamically without manually storing thousands of Pokémon records.

🗄️ SQLite Database

Although PokéAPI provides Pokémon information, PokeVerse also contains information specific to its own features.

SQLite is therefore used for internally managed content.

The database stores information for features such as:

Pokémon Games
Game Features
Game Challenges
Starter Pokémon
Legendary Pokémon
Related Games
Timeline Events

The database is located at:

database/pokeverse.db
🧩 Database Structure

The Games system uses multiple related tables.

games
   │
   ├── game_features
   ├── game_challenges
   ├── game_starters
   ├── game_legendaries
   └── related_games

The Timeline system maintains its own timeline event data.

Foreign keys are used where appropriate to maintain relationships between records.

🧠 Why Two Data Sources?

PokeVerse uses both PokéAPI and SQLite because they serve different purposes.

PokéAPI

Used for dynamic Pokémon-related information such as:

Pokémon
Types
Abilities
Evolution chains
Statistics
Artwork
SQLite

Used for PokeVerse-specific structured content such as:

Games encyclopedia information
Game challenges
Starters
Legendaries
Related games
Historical timeline events

This separation keeps the application organized and avoids unnecessarily duplicating Pokémon data.

🏗️ Application Architecture

PokeVerse follows a Flask-based web application architecture.

                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  Flask Routes │
                    └───────┬───────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       ┌──────────────┐           ┌──────────────┐
       │   PokéAPI    │           │    SQLite    │
       └──────┬───────┘           └──────┬───────┘
              │                           │
              └─────────────┬─────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Jinja2 HTML   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ HTML/CSS/JS   │
                    └───────────────┘
📁 Project Structure
PokeVerse/
│
├── app.py
├── requirements.txt
├── README.md
├── timeline.sql
│
├── database/
│   ├── pokeverse.db
│   ├── setup_db.py
│   ├── insert_games.py
│   ├── insert_features.py
│   ├── insert_challenges.py
│   ├── insert_starters.py
│   ├── insert_legendaries.py
│   ├── insert_related.py
│   └── insert_timeline.py
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   ├── games.css
│   │   ├── pokemon_details.css
│   │   ├── random.css
│   │   ├── tdetails.css
│   │   └── timeline.css
│   │
│   ├── js/
│   │   └── random.js
│   │
│   └── images/
│       ├── cards/
│       ├── games/
│       ├── icons/
│       ├── overview/
│       ├── region/
│       └── timeline/
│
└── templates/
    ├── index.html
    ├── pokemon_hub.html
    ├── pokemon_details.html
    ├── quiz.html
    ├── random.html
    ├── type_details.html
    ├── timeline.html
    │
    └── games/
        ├── games_home.html
        └── game_details.html
⚙️ Local Installation
1. Clone the repository
git clone https://github.com/soumik-85/Pokeverse.git
2. Open the project
cd Pokeverse
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py

The application will then be available locally through Flask.

📦 Requirements

The main dependencies are:

Flask==3.1.0
requests==2.34.2
gunicorn

Python standard-library modules such as random and sqlite3 do not need to be installed separately.

🔐 Environment Variables

PokeVerse uses an environment variable for the Flask secret key in production.

SECRET_KEY

The application reads the value using:

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "pokeverse_master_challenge"
)

The production secret is stored in the hosting platform rather than being exposed in the source code.

🚀 Deployment

PokeVerse is deployed using Render.

Deployment Workflow
Local Development
       ↓
Git
       ↓
GitHub
       ↓
Render
       ↓
Install Requirements
       ↓
Gunicorn
       ↓
Live Website
Build Command
pip install -r requirements.txt
Start Command
gunicorn app:app
Live Website

🌐 https://pokeverse-lgf.onrender.com

🔄 Development Workflow

The typical development workflow is:

Make changes
     ↓
Test locally
     ↓
git status
     ↓
git add .
     ↓
git commit
     ↓
git push origin main
     ↓
Render automatically redeploys
     ↓
Updated PokeVerse
🧪 Testing

Major PokeVerse features were tested during development, including:

Home page navigation
Pokémon search
Pokémon details
Type Explorer
Evolution Explorer
Type Effectiveness
Quiz modes
Quiz sessions and scoring
Games pages
Game details
Timeline navigation
Timeline animations
SQLite database queries
Static image loading
GitHub deployment
Production deployment

All four quiz modes were also tested after the production configuration changes to ensure the quiz system continued to work correctly.

🛠️ Challenges During Development

Building PokeVerse involved more than creating individual pages.

API Integration

Working with an external API required handling API responses, extracting the required information, displaying dynamic data, and dealing with API-dependent features.

Database Design

The Games and Timeline sections required structured application-owned data, which led to designing SQLite tables and relationships instead of storing everything directly inside HTML.

Dynamic Templates

Jinja2 was used to pass backend data into HTML templates and generate pages dynamically.

Interactive UI

JavaScript was used for interactions such as quiz behavior, timeline event selection, and dynamic interface updates.

Debugging

The project involved solving template errors, database issues, styling problems, scrolling behavior, timeline alignment, JavaScript interactions, and deployment configuration issues.

Deployment

The project also required understanding how a development Flask application is prepared for production.

This included:

requirements.txt
Environment variables
Gunicorn
GitHub integration
Render configuration
Production startup commands
🎯 Project Goals

The main goals of PokeVerse were:

Build a complete Pokémon information platform.
Learn how to consume and use a real REST API.
Understand Flask backend development.
Work with a relational database.
Create dynamic web pages using Jinja2.
Build interactive frontend features with JavaScript.
Organize a larger project into maintainable files and modules.
Use Git and GitHub for version control.
Deploy a Flask application to the internet.
Understand the complete journey from development to production.
🔮 Future Improvements

Possible future improvements include:

User accounts
Favorite Pokémon
Personal Pokédex
Advanced Pokémon comparison
More detailed game information
Advanced search
Additional quiz modes
Leaderboards
User quiz history
More timeline events
Media section
Better mobile optimization
Persistent cloud database
Performance optimization
Caching frequently requested API data
📚 What This Project Taught Me

PokeVerse became more than a collection of web pages.

Through the project, I gained practical experience with:

Python
Flask
REST APIs
PokéAPI
SQLite
SQL
Jinja2
HTML
CSS
JavaScript
Git
GitHub
Environment variables
Gunicorn
Cloud deployment
Debugging
Project organization

Most importantly, the project helped me understand the complete development cycle:

Idea
 ↓
Planning
 ↓
Development
 ↓
API Integration
 ↓
Database Design
 ↓
Frontend Development
 ↓
Debugging
 ↓
Version Control
 ↓
Deployment
 ↓
Live Application
👨‍💻 Developer

Soumik Adhikary

B.Tech Computer Engineering Student

🐙 GitHub:
https://github.com/soumik-85

📌 Project Status

🟢 Live and Deployed

PokeVerse is currently available online as a personal learning and portfolio project.

⭐ Explore PokeVerse

🌐 Live Website:
https://pokeverse-lgf.onrender.com

🐙 GitHub Repository:
https://github.com/soumik-85/Pokeverse

❤️ Built with curiosity, debugging, and a lot of Pokémon.