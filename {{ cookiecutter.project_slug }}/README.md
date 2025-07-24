# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

---

## Features

This project template comes equipped with:

* **Django {{ cookiecutter.django_version }}**: The web framework for perfectionists with deadlines.
* **Django REST Framework {{ cookiecutter.drf_version }}**: Powerful and flexible toolkit for building Web APIs.
* **OpenAPI/Swagger Documentation**: Automatically generated interactive API documentation using `drf-spectacular`, accessible at the base URL.
* **Token Authentication**: Secure API access using DRF's Token Authentication.
* **`uv`**: A fast Python package installer and resolver.
* **`ruff`**: An extremely fast Python linter and formatter.
* **`pre-commit`**: Automates code quality checks before committing.
* **`pytest`**: Robust testing framework for your API endpoints.
* **SQLite Database**: Default database for easy local development.

## Getting Started

Follow these steps to set up and run your {{ cookiecutter.project_name }} project.

### Prerequisites

* Python {{ cookiecutter.python_version }} or higher
* `uv` (recommended, install with `pip install uv`) or `pip`

### 1. Generate the Project

First, ensure you have Cookiecutter installed:
```bash
pip install cookiecutter
```

Then, navigate to the directory where your `cookiecutter-django-rest-api` template is located (the folder containing `cookiecutter.json`) and run:
```bash
cookiecutter ./cookiecutter-django-rest-api
```
Follow the prompts to configure your new project. This will create a new directory with your chosen `project_slug`.

### 2. Install Dependencies

Navigate into your newly generated project directory:
```bash
cd {{ cookiecutter.project_slug }}
```

Install the project dependencies using `uv`:
```bash
uv sync --dev
```

### 3. Database Migrations

This project uses a `Car` model which should have its table named `car`. If you're running this for the very first time, or if you previously ran migrations before this `db_table` setting was applied, you might need to clean up first.

**First-time setup or if you faced `api_car` issues previously:**

1.  Delete the existing SQLite database file (if it exists):
    ```bash
    rm db.sqlite3 # On Linux/macOS
    # Or on Windows: del db.sqlite3
    ```
2.  Delete any existing migration files for the `api` app (except `__init__.py`):
    ```bash
    rm api/migrations/00*.py # On Linux/macOS
    # Or on Windows: del api\migrations\00*.py
    ```

**Then, apply the migrations:**

1.  Create migration files for your `api` app:
    ```bash
    uv run manage.py makemigrations api
    ```
2.  Apply all pending database migrations:
    ```bash
    uv run manage.py migrate
    ```

### 4. Create a Superuser

You'll need an administrator account to access the Django admin panel and to generate API tokens for testing protected endpoints.

```bash
uv run manage.py createsuperuser
```
Follow the prompts to set up your username, email, and password.

### 5. Generate an API Authentication Token

Your API uses Token Authentication. To access protected endpoints, you'll need a token.

1.  Ensure your Django development server is **not** running.
2.  Generate a token for your superuser:
    ```bash
    uv run manage.py drf_create_token <your_superuser_username>
    ```
    (Replace `<your_superuser_username>` with the username you created in the previous step.)
    **Copy the generated token string.**

### 6. Run the Development Server

```bash
uv run manage.py runserver
```

### 7. Access the API and Swagger UI

* **Swagger UI (Interactive API Docs):** Open your web browser and navigate to `http://127.0.0.1:8000/`. You should be redirected to the interactive Swagger UI.
* **API Endpoints:** Your API endpoints are now directly available at the root (e.g., `http://127.0.0.1:8000/cars/`).

#### Authorizing in Swagger UI

To interact with protected endpoints (POST, PUT, PATCH, DELETE) in the Swagger UI:

1.  Click the green **"Authorize"** button in the top right corner.
2.  In the dialog, find the input field under `Token (apiKey)`.
3.  Paste your copied token, prefixed with `Token ` (e.g., `Token 9e6ef7f5b3f1c2d4e8a7b6c5d4f3e2a1b9c8d7e6`).
4.  Click **"Authorize"** then **"Close"**.

Now you can try out all API methods.

#### Example Authenticated Request (using `curl`)

```bash
curl -X POST \
  http://127.0.0.1:8000/cars/ \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Token YOUR_AUTH_TOKEN_HERE' \
  -d '{
    "make": "Tesla",
    "model": "Model Y",
    "year": 2023
  }'
```
Remember to replace `YOUR_AUTH_TOKEN_HERE` with your actual token.

### 8. Running Tests

You can run the built-in tests using `pytest` or Django's `manage.py test`:

```bash
pytest
# Or:
# uv run manage.py test
```

### 9. Using Pre-commit Hooks

This project includes `pre-commit` hooks to ensure code quality before commits.

1.  Install the hooks into your Git repository:
    ```bash
    pre-commit install
    ```
2.  Now, `ruff` formatting and linting (and tests) will automatically run before each `git commit`. If issues are found, the commit will be blocked, allowing you to fix them.

### 10. Environment Variables

Sensitive settings are managed via environment variables. A `.env.example` file is provided, which you can copy to `.env` and fill in your actual values.
```bash
cp .env.example .env
```

Remember to keep your `.env` file out of version control (it's already included in `.gitignore`).
