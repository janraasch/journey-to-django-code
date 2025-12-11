# Journey to Django

Source code for my talk **Journey to Django** at the [Ruby Usergroup Hamburg 🇩🇪](https://hamburg.onruby.de/) (December 2025).

🔋 This branch includes some more batteries than the [`main`](https://github.com/janraasch/journey-to-django-code) branch:

* [just](https://just.systems/) for running commands
* [djhtml](https://github.com/rtts/djhtml) for checking HTML templates
* [ruff](https://docs.astral.sh/ruff/) for linting and formatting code

## Working with the App

```bash
# Install uv
# brew install uv
# see https://docs.astral.sh/uv/

# Install just
# brew install just
# see https://just.systems/

# Clone the repository, then
cd journey-to-django-code

# Setup
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser

# Run the development server
just dev

# Run tests
just test

# Check linting (no fixes)
just lint

# Format code
just fmt

# Run CI (lint + test)
just ci
```

## ⛴️ Even more batteries / Deploying the App

Check out [django-simple-deploy](https://django-simple-deploy.readthedocs.io/en/latest/) to get this puppy deployed to a server in no time.

## Links

**Talk details:** [hamburg.onruby.de/topics/django-from-a-rails-perspective-3174](https://hamburg.onruby.de/topics/django-from-a-rails-perspective-3174)

**Meetup details:** [hamburg.onruby.de/events/christmas-ruby-usergroup-hamburg-december-2025-2168](https://hamburg.onruby.de/events/christmas-ruby-usergroup-hamburg-december-2025-2168)

## License

MIT
