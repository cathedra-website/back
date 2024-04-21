# Используем базовый образ Python
FROM python:3.10-slim-bullseye as python-base

# Установка переменных окружения для Python и Poetry
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

# Добавление Poetry и виртуальной среды в PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Этап сборки для установки зависимостей
FROM python-base as builder-base

RUN apt-get update && apt-get -y install libpq-dev gcc

# Установка Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Копирование файлов зависимостей Poetry
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Установка зависимостей проекта
RUN poetry config virtualenvs.create false && poetry install --no-dev
RUN poetry add gunicorn

# Финальный этап сборки проекта
FROM python-base as production

# Копирование установленных зависимостей
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
COPY . /app/

# Установка рабочей директории приложения
WORKDIR /app

# Открытие порта для Gunicorn
EXPOSE 8000

# Команда для запуска приложения через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]
