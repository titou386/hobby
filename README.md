# hobby
## Django Blog & Portfolio

> A personal blog about programming, computer science, 3D printing and AI — also a showcase of my development skills.

---

## About

This is a personal blog built with Django and its native templating system. The goal is to share articles on technical topics while demonstrating hands-on development skills through the project itself.

---

## Tech stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| Framework | Django |
| Templates | Django template engine |
| Database (dev) | SQLite |
| Database (prod) | Postgres|
| Auth | Django built-in auth |

---

## Project structure

```
project/
├── manage.py
├── core/ 
|   ├── urls.py
|   ├── wsgi.py                 
│   └── settings/           # Settings, urls, wsgi
│       ├── base.py
|       ├── dev.py
│       └── prod.py
├── users/                   # Authentication and user profiles
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── blog/                    # Articles, categories, tags
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── comments/            # Comment system
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
├── static/
└── requirements.txt
```

---

## Django apps

### `users`
Handles authentication and user profiles.
- Custom user model (extends AbstractUser)
- Register / login / logout / change password
- Author profile

### `blog`
Core of the project. Manages article publishing.
- Articles with title, slug, content, cover image
- Draft / published status
- Categories and tags
- Author linked to `users`

### `comments`
Comment system attached to articles.
- Comments linked to an article and a user
- Basic moderation

---

## Current roadmap

- [x] Core models (users, blog, comments)
- [x] Authentication
- [ ] Views and templates
- [ ] Categories and tags
- [ ] Draft management
- [ ] Pagination and search
- [ ] Responsive design
- [ ] Deployment

---

## Local setup

```bash
# Clone the repo
git clone <repo-url>
cd <project-name>

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

---

## Environment variables

Create a `.env` file at the root (for deployement see the example):

```env
SECRET_KEY=your_django_secret_key
```

---

## Blog topics

- **Programming** — Python, Django, best practices, tutorials
- **Computer science** — architecture, networking, systems
- **3D printing** — materials, slicers, projects
- **Artificial intelligence** — LLMs, tools, hands-on experiments

---

## Author

Personal project — blog and development portfolio.
