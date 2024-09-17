# Django Task Management App

## Overview

This is a Django-based task management application with features including task and tag management. The project includes RESTful APIs for tasks and tags with a custom user model and permissions system. API documentation is available via Swagger and ReDoc.

## Project Structure

- **common/**: Contains common utilities and abstract models.
- **config/**: Django configuration files including settings, URLs, and ASGI/WSGI configurations.
- **tasks/**: Application for task management including models, views, serializers, and selectors.
- **users/**: Application for user management with custom user model and admin configurations.
- **docker-compose.dev.yml**: Development Docker Compose configuration.
- **docker-compose.yml**: Production Docker Compose configuration.
- **manage.py**: Django project management script.
- **requirements.txt**: Python package dependencies.
- **ruff.toml**: Ruff configuration file.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/md5502/your-repository.git
    cd your-repository
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv .env
    source .env/bin/activate  # On Windows use `.env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Docker Setup

To run the application using Docker, use the following commands:

1. **Build and start the containers:**

    ```sh
    docker-compose -f docker-compose.yml up --build
    ```

2. **For development, use:**

    ```sh
    docker-compose -f docker-compose.dev.yml up --build
    ```

## API Documentation

- **Swagger UI**: Provides interactive API documentation. Access it at `http://localhost:8000/` when the server is running.
- **ReDoc**: Provides a static, user-friendly API documentation. Access it at `http://localhost:8000/redoc/` when the server is running.

## Usage

- **Tasks API:**
  - `GET /tasks/`: List all tasks
  - `POST /tasks/`: Create a new task
  - `GET /tasks/{id}/`: Retrieve a task by ID
  - `PUT /tasks/{id}/`: Update a task by ID
  - `DELETE /tasks/{id}/`: Delete a task by ID

- **Tags API:**
  - `GET /tags/`: List all tags
  - `POST /tags/`: Create a new tag
  - `GET /tags/{id}/`: Retrieve a tag by ID
  - `PUT /tags/{id}/`: Update a tag by ID
  - `DELETE /tags/{id}/`: Delete a tag by ID

## Permissions

- **Task Endpoints:**
  - Users can only view, update, or delete tasks they own.

- **Tag Endpoints:**
  - Users can view, create, update, or delete tags.

## Custom Commands

- **Generate Fake Data:**

    ```sh
    python manage.py generate_fake_data
    ```

## Contributing

1. **Fork the repository**
2. **Create a new branch:**

    ```sh
    git checkout -b feature/your-feature
    ```

3. **Commit your changes:**

    ```sh
    git commit -m "Add some feature"
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature/your-feature
    ```

5. **Create a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [md5502](mailto:m.baniasadi.d@gmail.com).

