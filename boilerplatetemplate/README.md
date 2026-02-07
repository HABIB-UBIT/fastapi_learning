# Juno Backend

Backend for the Juno social meetup application.

## Setup

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables:**

    Copy `.env.example` to `.env` and fill in your values.

    ```bash
    cp .env.example .env
    ```

    *   `DATABASE_URL`: Your PostgreSQL connection string.
    *   `SUPABASE_URL` & `SUPABASE_KEY`: Your Supabase project credentials.
    *   `GOOGLE_MAPS_API_KEY`: Your Google Maps API key.

4.  **Database Migrations:**

    Run migrations to create the database schema:

    ```bash
    alembic upgrade head
    ```

5.  **Run the Application:**

    ```bash
    uvicorn app.main:app --reload
    ```

## Project Structure

The project follows a **Modular Monolith** architecture.

*   `app/`
    *   `core/`: Shared configuration (`config.py`) and utilities.
    *   `db/`: Database connection (`session.py`) and base models (`base.py`).
    *   `modules/`: Feature-specific modules.
        *   `auth/`: Authentication and User management.
        *   `events/`: Event creation and discovery.
        *   `chat/`: Real-time messaging.
        *   `maps/`: Google Maps integration.
        *   *Each module contains:*
            *   `models.py`: SQLAlchemy database models.
            *   `schemas.py`: Pydantic models for request/response.
            *   `router.py`: API route handlers.
            *   `service.py`: Business logic (optional).
    *   `main.py`: Application entry point and router registration.
*   `alembic/`: Database migration scripts.
