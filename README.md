# Journey to Django

Source code for my talk **Journey to Django** at the [Ruby Usergroup Hamburg 🇩🇪](https://hamburg.onruby.de/) (December 2025).

## Running the App

```bash
# Install uv
# see https://docs.astral.sh/uv/

# Clone the repository, then
cd journey-to-django-code

# Setup
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser

# Run the development server
uv run python manage.py runserver
```

## 🔋 More Batteries

Check out the [`more-batteries` branch](https://github.com/janraasch/journey-to-django-code/tree/more-batteries) for code formatting, linting and a task runner.

## Links

**Talk details:** [hamburg.onruby.de/topics/django-from-a-rails-perspective-3174](https://hamburg.onruby.de/topics/django-from-a-rails-perspective-3174)

**Meetup details:** [hamburg.onruby.de/events/christmas-ruby-usergroup-hamburg-december-2025-2168](https://hamburg.onruby.de/events/christmas-ruby-usergroup-hamburg-december-2025-2168)

## License

MIT
