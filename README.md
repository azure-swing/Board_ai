# AI.Director - Storyboard AI Editor

A powerful, AI-driven storyboard editing platform designed for creators, video editors, and AI enthusiasts. AI.Director allows users to create, manage, and generate video content frame-by-frame with integrated AI models.

## 🚀 Features

- **Project Management**: Organize your creative work into specific projects with titles, descriptions, and custom settings.
- **Shot-Based Editing**: Granular control over every individual shot (scene) in your project.
- **AI-Powered Generation**: Integrated support for top-tier AI models like **Runway Gen-3 Alpha**, **Sora**, and **Kling 1.5** for high-quality video generation.
- **Interactive Timeline**: A modern, responsive workspace including a drag-and-drop timeline for sequence reordering and shot duration adjustment.
- **Media Asset Integration**: Upload reference images or videos as reference frames for AI generation.
- **Audio Support**: Upload background music and preview its timing against your scenes.
- **Dynamic Real-time Preview**: View your shots and AI-generated outputs instantly in the storyboard workspace.

## 🛠️ Technology Stack

### Frontend
- **Vue.js 3**: Progressive JavaScript framework for building a responsive UI.
- **Tailwind CSS**: Modern utility-first CSS framework for high-end aesthetics.
- **Font Awesome**: iconography for a professional look and feel.

### Backend
- **FastAPI**: High-performance Python-based API for handling project data and AI integration.
- **SQLAlchemy & SQLite**: Robust data persistence and local database management.

## 📦 Getting Started

### 1. Backend Setup
Navigate to the `backend` directory and install dependencies:
```bash
cd backend
pip install -r requirements.txt
```
*Note: Ensure you have `fastapi`, `uvicorn`, `sqlalchemy`, and potentially `databases` installed.*

Run the server:
```bash
uvicorn main:app --reload
```

### 2. Frontend Setup
Simply open `board.html` or `main.html` in your browser. (Alternatively, serve it with a VS Code Live Server).

## 📊 Database Schema
The project uses a localized SQLite database (`director.db`) by default.
- **Projects**: Core project containers.
- **Shots**: Individual scene blocks within each project.

---

Created with ❤️ by the Board_ai team.
