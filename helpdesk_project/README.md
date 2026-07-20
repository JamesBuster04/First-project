# Help Desk Ticketing System (Beginner Django + Postgres + REST API)

A small but real project you can grow as you learn. It models the tickets you
already deal with at your Level 1 help desk job: each ticket has a title,
description, status, priority, a category, an assignee, and comments.

It is built with:
- **Python** — the language
- **Django** — the web framework
- **Django REST Framework** — turns your data into a JSON API
- **SQLite** by default, **PostgreSQL** when you are ready (instructions below)
- **VS Code** — your editor

---

## 1. What you will learn (in order)

1. How a Django project is structured (projects vs apps, settings, urls).
2. Models = database tables described in Python.
3. Migrations = how Django creates/updates those tables safely.
4. The Django admin = a free CRUD UI for your data.
5. A REST API = how other apps (or a future frontend) talk to your data.
6. PostgreSQL = swapping SQLite for a "real" production database.
7. (Later) Authentication, a real frontend, automated tests, deployment.

---

## 2. First-time setup

Open a terminal **inside this folder** (in VS Code: Terminal > New Terminal).

### a) Create a virtual environment
A virtual environment keeps this project's packages separate from the rest of
your computer. Run this once:

    python -m venv venv

Then activate it (Windows, in the VS Code terminal / Git Bash):

    source venv/Scripts/activate

(You should see `(venv)` appear at the start of your prompt.)

### b) Install the dependencies
    pip install -r requirements.txt

### c) Create the database tables
    python manage.py migrate

### d) Add sample data
    python manage.py seed

### e) (Optional) Create your own admin login
    python manage.py createsuperuser

### f) Run the server
    python manage.py runserver

Now open these in your browser:
- http://127.0.0.1:8000/admin/  -> the admin panel (login admin / admin123 from the seed, or your own user)
- http://127.0.0.1:8000/api/    -> the API home (browsable web UI)

---

## 3. Try the API

List tickets:
    GET http://127.0.0.1:8000/api/tickets/

Create a ticket (POST, body as JSON):
    {
      "title": "Printer offline",
      "description": "User cannot print to the 2nd floor printer.",
      "priority": "HIGH",
      "category_id": 1
    }

Ticket stats:
    GET http://127.0.0.1:8000/api/tickets/stats/

Add a comment to ticket #1:
    POST http://127.0.0.1:8000/api/tickets/1/add_comment/
    { "body": "Rebooted the print server." }

You can do all of this from the browsable UI at /api/ by clicking through, or
with a tool like Postman / Thunder Client (a VS Code extension).

---

## 4. Switching to PostgreSQL (the "real" database)

Companies almost always use PostgreSQL. This is a great next learning step.

1. Install PostgreSQL (https://www.postgresql.org/download/windows/) and
   remember the password you set for the `postgres` superuser.
2. Open the `psql` shell or pgAdmin and create a database + user:
       CREATE DATABASE helpdesk;
       CREATE USER helpdesk_user WITH PASSWORD 'your_password';
       GRANT ALL PRIVILEGES ON DATABASE helpdesk TO helpdesk_user;
3. In `helpdesk_project/settings.py`, comment out the SQLite `DATABASES` block
   and uncomment the PostgreSQL block. Fill in your details.
4. Make sure `psycopg2-binary` is installed (it is already in requirements.txt).
5. Run `python manage.py migrate` again — this time it builds the tables in
   Postgres. Then `python manage.py seed`.

That's the whole difference between a learning database and a production one.

---

## 5. Good first changes to make (practice)

- Add a `due_date` field to Ticket and re-run `makemigrations` + `migrate`.
- Add a new status, e.g. "WAITING_ON_CUSTOMER", to the STATUS_CHOICES.
- Add an endpoint that lists only URGENT + OPEN tickets.
- Add basic authentication so the API requires a login (look up
  `rest_framework.authentication.TokenAuthentication`).
- Write a test in `tickets/tests.py` that creates a ticket and checks the API.

---

## 6. Project layout (where things live)

    helpdesk_project/
      manage.py                 # command-line entry point
      requirements.txt          # packages to install
      helpdesk_project/
        settings.py             # configuration (database, apps, API)
        urls.py                 # top-level routes (/admin/, /api/)
      tickets/                  # your app
        models.py               # the database tables (start here)
        serializers.py          # model <-> JSON
        views.py                # the API logic
        urls.py                 # API routes
        admin.py                # admin panel config
        management/commands/seed.py  # sample data generator
