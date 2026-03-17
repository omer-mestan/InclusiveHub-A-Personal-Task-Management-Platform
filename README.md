# InclusiveHub: A Personal Task Management Platform

InclusiveHub is a Flask-based web application for personal task management. It was created as a project focused on usability, structured backend logic, and a more accessible approach to organizing daily work.

The idea behind the platform is simple: give users a clear place where they can register, log in, manage their own tasks, and update their profile in a lightweight web application built with Python and Flask.

## Project Overview

The application allows users to:

- create an account
- log in securely
- create, edit, and delete personal tasks
- manage their own profile information
- view task-related data inside a dedicated task area

The project combines backend logic, database models, template-based rendering, and basic user session management in a single full-stack Flask application.

## Main Features

- user registration
- user login and logout
- password hashing
- session-based authentication
- task creation
- task editing
- task deletion
- personal task list view
- profile update page
- SQLAlchemy-based data models

## Included Data Models

The backend currently includes models for:

- `User`
- `Task`
- `Comment`

This provides a small but meaningful relational structure:

- each user can own multiple tasks
- tasks can include descriptions, due dates, and status
- comments are modeled in the database for future or extended interaction features

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Jinja templates

## Project Structure

Main files and folders:

- `app.py` - application routes and request handling
- `models.py` - database models
- `database.py` - SQLAlchemy setup
- `templates/` - HTML templates for pages such as login, register, tasks, and profile
- `static/style.css` - application styling

## Available Pages

The project includes several user-facing pages, such as:

- home page
- about page
- login page
- registration page
- tasks page
- new task page
- edit task page
- profile page

This gives the project a more complete full-stack structure than a simple single-page CRUD example.

## Authentication And Task Access

The application uses session-based authentication with Flask sessions.

This means:

- users must log in to access their task area
- only the owner of a task can edit or delete it
- user data is stored in the database
- passwords are stored as hashes, not plain text

## How To Run

Clone the repository:

```bash
git clone https://github.com/omer-mestan/InclusiveHub-A-Personal-Task-Management-Platform.git
cd InclusiveHub-A-Personal-Task-Management-Platform
```

Create and activate a virtual environment if needed:

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install flask flask-sqlalchemy werkzeug
```

Run the app:

```bash
python app.py
```

Then open:

- `http://127.0.0.1:5000/`

## Why This Project Matters

InclusiveHub is valuable as a portfolio project because it shows:

- practical Flask development
- user authentication logic
- task-based CRUD functionality
- relational data modeling
- template-driven full-stack structure
- a product-oriented idea rather than only isolated code exercises

It is also a good example of how to build a simple but complete web application from scratch using Python.

## Possible Future Improvements

Some good directions for extending the project:

- task status updates from the UI
- better task filtering and sorting
- comment creation and display in the interface
- form validation improvements
- responsive design upgrades
- role-based access or admin features
- deployment to a public hosting platform

## Author

**Yumer Mestan**  
GitHub: [omer-mestan](https://github.com/omer-mestan)
