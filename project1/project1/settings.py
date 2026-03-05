"""
settings.py
"""

# ============================================================
# IMPORTS
# ============================================================

from pathlib import Path
import os


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY SETTINGS
# ============================================================

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ["akward.onrender.com"]


# ============================================================
# INSTALLED APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'post.apps.PostConfig',

    'tailwind',
    'theme',
]

TAILWIND_APP_NAME = 'theme'


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URL & TEMPLATE CONFIGURATION
# ============================================================

ROOT_URLCONF = 'project1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ============================================================
# WSGI CONFIGURATION
# ============================================================

WSGI_APPLICATION = 'project1.wsgi.application'


# ============================================================
# DATABASE CONFIGURATION
# ============================================================

import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ============================================================
# STATIC FILES CONFIGURATION
# ============================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# ============================================================
# MEDIA FILES CONFIGURATION
# ============================================================

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ============================================================
# AUTHENTICATION & EMAIL SETTINGS
# ============================================================

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/post/list/'
LOGOUT_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")


# ============================================================
# SESSION CONFIGURATION
# ============================================================

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 600


# ============================================================
# NOTES
# ============================================================

"""
ABOUT THIS FILE
---------------
Core configuration file for the project.

This file controls:
    - Installed applications
    - Middleware
    - Database configuration
    - Authentication behavior
    - Static and media file handling
    - Template configuration

Keep this file clean and environment-aware.


BASE_DIR
--------
Root directory of the project.
Used to build absolute paths safely.


SECURITY SETTINGS
-----------------
SECRET_KEY
    Used for cryptographic signing.
    In production: NEVER hardcode. Store in environment variables.

DEBUG
    Always set to False in production.
    True exposes detailed error pages.

ALLOWED_HOSTS
    Define allowed domains when deploying.
    Example: ['yourdomain.com', 'www.yourdomain.com']


INSTALLED APPLICATIONS
-----------------------
'post.apps.PostConfig'
    Ensures signals are properly registered and
    custom app configuration is applied.

Standard Django core apps and third-party apps
(tailwind, theme) are also registered here.


MIDDLEWARE
----------
Processes requests globally before they reach views.
Order matters — do not rearrange without understanding the impact.


URL & TEMPLATE CONFIGURATION
-----------------------------
DIRS
    Points to the global templates directory.

APP_DIRS=True
    Enables templates inside individual app folders.


DATABASE CONFIGURATION
-----------------------
Currently configured for PostgreSQL (local development).
For production:
    - Ensure proper credentials are stored in environment variables.
    - Use managed PostgreSQL service (e.g., RDS, Supabase).


PASSWORD VALIDATION
--------------------
Validators protect against weak passwords.
Never disable in production.


STATIC FILES
------------
STATICFILES_DIRS
    Directory for custom CSS/JS assets.

STATIC_URL
    URL prefix for serving static files.


MEDIA FILES
-----------
MEDIA_ROOT
    Stores uploaded files (images, profile pictures).
    Must be configured correctly for ImageField to work.

MEDIA_URL
    URL prefix for serving media files.


AUTHENTICATION SETTINGS
------------------------
LOGIN_URL
    Redirect location when user tries to access a protected page.

LOGIN_REDIRECT_URL
    Where user lands after successful login.

LOGOUT_REDIRECT_URL
    Where user lands after logout.


EMAIL CONFIGURATION
--------------------
Configured for Gmail SMTP with TLS.
EMAIL_HOST_PASSWORD should use a Gmail App Password, not your main password.
In production: store credentials in environment variables.


SESSION CONFIGURATION
----------------------
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    Session ends when the browser is closed. No persistent cookie.

SESSION_COOKIE_AGE = 600
    Session also expires after 600 seconds (10 minutes) of inactivity.


IMPORTANT PRODUCTION NOTES
---------------------------
1. Never keep DEBUG=True in production.
2. Move SECRET_KEY to environment variables.
3. Configure ALLOWED_HOSTS before deployment.
4. Store all credentials (DB, email) in environment variables.
5. Use WhiteNoise or a CDN for static files in production.
6. Use proper media storage (S3 or similar) for scaling.
7. Keep settings separated for development, production, and testing.
"""
