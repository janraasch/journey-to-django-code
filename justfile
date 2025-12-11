# Default task
default:
    @just --list

# Run development server
dev:
    uv run python manage.py runserver

# Run tests
test:
    uv run python manage.py test

# Check linting (no fixes)
lint:
    uv run ruff format --check .
    uv run ruff check .
    uv run djhtml --check wishes/templates/

# Format code
fmt:
    uv run ruff format .
    uv run ruff check --fix .
    uv run djhtml wishes/templates/

# CI: lint + test
ci: lint test
