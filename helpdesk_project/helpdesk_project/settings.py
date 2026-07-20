"""
Django settings for the Help Desk project.

This file is the "control panel" for your project. You normally only need
to touch a few things here. The most important one for you right now is the
DATABASES setting near the bottom.
"""

from pathlib import Path

# BASE_DIR is the folder that contains this project (used for file paths).
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# This value is fine for local learning. In a real app you would load it
# from an environment variable so it is never written in code.
SECRET_KEY = "django-insecure-dev-only-change-me-before-deploy-abcdef123456"

# DEBUG = True shows helpful error pages while you learn. NEVER set this to
# False on a public server without also setting up real security.
DEBUG = True

# Which addresses are allowed to visit the site. localhost is fine for learning.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# ---------------------------------------------------------------------------
# APPLICATIONS
# "django.contrib.*" are built-in Django features. "rest_framework" is the
# API toolkit. "tickets" is the app YOU will build your logic in.
# ---------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "tickets",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "helpdesk_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "helpdesk_project.wsgi.application"

# ---------------------------------------------------------------------------
# DATABASE
# ---------------------------------------------------------------------------
# By DEFAULT we use SQLite. It is a single file (db.sqlite3) and needs ZERO
# installation, so you can run this project immediately.
#
# When you are ready to learn PostgreSQL (a "real" database used in most
# companies), do two things:
#   1. Comment out the SQLite block below.
#   2. Uncomment the PostgreSQL block and fill in your database details.
#   3. Make sure psycopg2-binary (already in requirements.txt) is installed.
# ---------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "helpdesk",           # the database you create in Postgres
#         "USER": "helpdesk_user",      # the Postgres user you create
#         "PASSWORD": "your_password",  # that user's password
#         "HOST": "127.0.0.1",          # localhost
#         "PORT": "5432",               # default Postgres port
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------------------------------------------------
# REST FRAMEWORK
# This configures the API. For learning we allow anonymous access so you can
# try the API without logging in. In a real app you would require auth.
# ---------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",  # the nice web UI at /api/
    ],
}
