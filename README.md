# 😬 AwkwardPost — Share Your Most Awkward Moments

A full-stack **social media web application** built with Django where users can share, read, and engage with the most awkward moments of their lives. Features a complete authentication system with **email OTP verification**, automatic profile creation, session management, and full **CRUD operations** on posts.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Server](#running-the-server)
- [App Overview](#app-overview)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## 📌 About the Project

**AwkwardPost** is a community-driven platform where people can anonymously or publicly share embarrassing, funny, or relatable moments from their lives. Built on Django's MTV architecture, the app handles everything from user registration with OTP-based email verification to full post management — all wrapped in a clean, responsive UI.

---

## ✨ Features

### 🔐 Authentication & Security
- User registration with **email OTP verification** (via Django signals + email backend)
- Secure login / logout with **session handling**
- Password-protected routes using Django's `@login_required` decorator

### 👤 User Profiles
- **Automatic profile creation** on registration via Django signals (`post_save`)
- Profile view and edit functionality
- Profile picture support via static media

### 📝 Posts (CRUD)
- **Create** — Submit your awkward moment with a title and description
- **Read** — Browse all posts on the feed (`post_list`) or view a single post (`post_detail`)
- **Update** — Edit your own posts (`post_form`, `profile_edit`)
- **Delete** — Remove posts with a confirmation step (`post_delete_confirm`)

### 🌐 Additional Pages
- About, Contact, Privacy Policy, and Terms pages
- Responsive layout using custom CSS (`layout.css`, `post.css`)
- Theme app for shared static assets

---

## 🛠️ Tech Stack

| Layer            | Technology                        |
|------------------|-----------------------------------|
| Backend          | Python 3, Django                  |
| Frontend         | HTML5, CSS3                       |
| Templating       | Django Template Engine            |
| Database         | SQLite (default), configurable    |
| Email            | Django Email Backend (OTP)        |
| Authentication   | Django Auth + Custom Signals      |
| Static Files     | Django Staticfiles                |

---

## 📁 Project Structure

```
DJANGOPROJECT1/
│
├── post/                             # Core app — posts & user profiles
│   ├── migrations/                   # Database migrations
│   ├── templates/                    # App-level HTML templates
│   │   ├── index.html                # Landing / home feed
│   │   ├── post_list.html            # All posts feed
│   │   ├── post_detail.html          # Single post view
│   │   ├── post_form.html            # Create / edit post form
│   │   ├── post_delete_confirm.html  # Delete confirmation
│   │   ├── profile.html              # User profile page
│   │   └── profile_edit.html         # Edit profile page
│   ├── admin.py                      # Admin panel registration
│   ├── apps.py
│   ├── forms.py                      # Django forms for posts & profiles
│   ├── models.py                     # Post and Profile models
│   ├── signals.py                    # Auto profile creation on registration
│   ├── urls.py                       # App-level URL routing
│   ├── utils.py                      # OTP generation & email utilities
│   └── views.py                      # All view logic
│
├── project1/                         # Django project config
│   ├── settings.py
│   ├── urls.py                       # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── static/                           # Global static files
│   ├── image/img.png
│   ├── layout.css
│   └── post.css
│
├── templates/                        # Global templates
│   ├── registration/
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── logged_out.html
│   │   └── verify_otp.html           # OTP verification page
│   ├── about.html
│   ├── contact.html
│   ├── layout.html                   # Base template (extended by all pages)
│   ├── privacy.html
│   └── terms.html
│
├── theme/                            # Theme app (shared UI assets)
├── manage.py
├── notes.md
└── requirement.txt
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Git
- A valid email account for OTP emails (Gmail recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Mohit-368/Akward-django-project.git
cd Akward-django-project
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirement.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser** *(optional, for admin access)*

```bash
python manage.py createsuperuser
```

### Environment Variables

Create a `.env` file in the root directory and configure the following:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

> ⚠️ For Gmail, use an **App Password** — not your regular password. Enable 2FA in your Google account, then generate one at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).

### Running the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

Admin panel: `http://127.0.0.1:8000/admin/`

---

## 🗺️ App Overview

| URL Pattern            | Page / Action            | Auth Required |
|------------------------|--------------------------|---------------|
| `/`                    | Home / Feed              | ❌            |
| `/register/`           | Register new user        | ❌            |
| `/verify-otp/`         | Email OTP verification   | ❌            |
| `/login/`              | Login                    | ❌            |
| `/logout/`             | Logout                   | ✅            |
| `/posts/`              | All posts list           | ❌            |
| `/posts/<id>/`         | Post detail view         | ❌            |
| `/posts/new/`          | Create new post          | ✅            |
| `/posts/<id>/edit/`    | Edit post                | ✅            |
| `/posts/<id>/delete/`  | Delete post              | ✅            |
| `/profile/`            | View profile             | ✅            |
| `/profile/edit/`       | Edit profile             | ✅            |

---

## ⚙️ Configuration

For **production** deployment, update `settings.py`:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

Then collect static files:

```bash
python manage.py collectstatic
```

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/awesome-feature`
3. Commit your changes: `git commit -m 'Add awesome feature'`
4. Push to the branch: `git push origin feature/awesome-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Built with 😬 and Django — because everyone has an awkward story to tell.
