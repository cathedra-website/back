FROM python:3.10-slim-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM python-base as builder-base

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN pip install "poetry==$POETRY_VERSION" && poetry --version

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH
COPY pyproject.toml ./

# Установка зависимостей проекта
RUN poetry install


###############################################
# Production Image
###############################################
FROM python-base as production
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY . /app/
WORKDIR /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]