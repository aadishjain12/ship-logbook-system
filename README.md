# ship-logbook-system

# 🚢 Ship Logbook System with NLP-based Voice Log Processing

A full-stack maritime logbook platform that replaces traditional paper-based log entries with a digital, voice-enabled, and automation-ready system. Built with the MERN stack, Flask, and NLP, it enables real-time, structured data capture for ship operations while ensuring security, compliance, and usability across roles.

---

## 🔧 Features

- ✅ Voice-to-Text Log Processing using NLP (spaCy)
- 🌍 Real-time GPS & Weather Data Integration
- 🔐 Role-Based Access Control (Crew, Admin, Inspector)
- 📊 Visual Reports using Chart.js and Leaflet.js
- 🧠 Automatic Error Validation & Structured Storage
- 📁 Secure Data Logging with SQLite & MongoDB
- 📈 Real-Time Dashboard & Report Generation
- ☁️ Cloud & Local Storage Support with Data Backups

---

## 🖥️ Tech Stack

| Category         | Tools/Technology                           |
|------------------|---------------------------------------------|
| Frontend         | React.js, Tailwind CSS                     |
| Backend          | Flask (Python), Node.js, Express.js        |
| Database         | SQLite (Local), MongoDB (NoSQL)            |
| Authentication   | JSON Web Token (JWT)                       |
| NLP Module       | spaCy                                      |
| APIs             | OpenMeteo, AIS, GPS                        |
| Deployment       | Railway, GitHub                            |
| Visualization    | Chart.js, Leaflet.js                       |
| Dev Tools        | Postman, Git, GitHub, VS Code              |

---

## 🧭 System Architecture

A modular 3-tier system:
- **Frontend**: React UI for logs, voice uploads, analytics
- **Backend**: Express & Flask APIs for log processing, NLP, authentication
- **Database**: MongoDB/SQLite storing structured logs and user metadata

---

## 📦 Installation & Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/ship-logbook-system.git
   cd ship-logbook-system
