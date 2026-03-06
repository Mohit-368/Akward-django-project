# Contributing to Akward 🎉

Thank you for your interest in contributing to **Akward** — a full stack social media platform built with Django and PostgreSQL where people share real life awkward moments. We welcome contributors of all skill levels and are excited to build this together!

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Setting Up Locally](#setting-up-locally)
- [Branching Guidelines](#branching-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Labels](#issue-labels)
- [Good First Issues](#good-first-issues)

---

## 📜 Code of Conduct

By participating in this project, you agree to maintain a respectful, inclusive, and harassment free environment for everyone. Be kind, be constructive, and help each other grow.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or above
- PostgreSQL installed and running
- Git
- A Gmail account for OTP email testing

### Setting Up Locally

1. **Fork the repository** by clicking the Fork button on the top right of the GitHub page.

2. **Clone your fork**

```bash
git clone https://github.com/your-username/Akward-django-project.git
cd Akward-django-project
```

3. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirement.txt
```

5. **Create a `.env` file** in the root directory and add the following:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

DATABASE_NAME=your-db-name
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

6. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Run the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the app running locally.

---

## 🤝 How to Contribute

### Step 1 — Find or Create an Issue

Browse the [Issues](https://github.com/Mohit-368/Akward-django-project/issues) tab and pick one that interests you. If you want to work on something not listed, open a new issue describing your idea before starting work.

### Step 2 — Get Assigned

Comment on the issue saying you would like to work on it. Wait for the project admin to assign it to you before starting. This avoids duplicate work.

### Step 3 — Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### Step 4 — Make Your Changes

Write clean, readable, and well commented code. Make sure your changes do not break existing functionality.

### Step 5 — Test Your Changes

Run the development server and manually verify your feature works as expected before submitting.

### Step 6 — Commit and Push

```bash
git add .
git commit -m "feat: add your feature description"
git push origin feature/your-feature-name
```

### Step 7 — Open a Pull Request

Go to your forked repo on GitHub and click **New Pull Request**. Fill in the PR template clearly describing what you changed and why.

---

## 🌿 Branching Guidelines

| Branch Type | Naming Convention | Example |
|---|---|---|
| Feature | feature/feature-name | feature/likes-system |
| Bug Fix | fix/bug-description | fix/otp-expiry-bug |
| Documentation | docs/what-you-updated | docs/update-readme |
| Refactor | refactor/what-you-changed | refactor/views-cleanup |

---

## ✍️ Commit Message Guidelines

Use clear and descriptive commit messages following this format:

```
type: short description
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat: add likes and comments to posts
fix: resolve OTP expiry not resetting correctly
docs: update setup instructions in README
```

---

## 🔍 Pull Request Process

- Make sure your branch is up to date with the main branch before opening a PR
- Fill out the PR description clearly explaining what was changed and why
- Link the related issue number in your PR description using `Closes #issue-number`
- PRs will be reviewed within 48 hours by the project admin
- Address all review comments before the PR can be merged
- Do not open PRs with unrelated changes bundled together

---

## 🏷️ Issue Labels

| Label | Meaning |
|---|---|
| `good first issue` | Perfect for first time contributors |
| `medium` | Requires some Django knowledge |
| `hard` | Advanced feature or architectural change |
| `bug` | Something is broken and needs fixing |
| `enhancement` | New feature or improvement |
| `documentation` | Improvements to docs or README |
| `help wanted` | Extra attention or expertise needed |

---

## 💡 Good First Issues

New to open source or Django? Start here:

- Add a character limit counter to the post creation form
- Improve error messages on the login and registration pages
- Add a loading state to the OTP verification button
- Improve mobile responsiveness of the post feed
- Add a back button to the post detail page

---

## 📬 Contact

Have questions? Feel free to open a [GitHub Discussion](https://github.com/Mohit-368/Akward-django-project/discussions) or reach out via the Issues tab. The project admin will respond within 48 hours.

---

> Built with 😬 and Django — because everyone has an awkward story to tell. Happy contributing!
