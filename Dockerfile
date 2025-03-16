FROM python:3.13-slim-bookworm

# Copy the uv binary from their image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL authors="Andrew"

COPY . /app
WORKDIR /app

RUN apt update && \
    apt upgrade -y && \
    apt install gcc libpq-dev build-essential -y && \
    apt clean

# Install the project's dependencies
RUN uv python install && \
    uv venv && \
    uv sync --frozen

EXPOSE 8000

# We only need to run `gunicorn` as long as the `gunicorn.conf.py` file is present
ENTRYPOINT ["uv", "run", "gunicorn"]