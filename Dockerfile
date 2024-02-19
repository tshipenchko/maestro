FROM python:3.11-slim-bookworm as builder
WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry==1.7.1
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true && \
    poetry install --only main --no-interaction --no-root

FROM python:3.11-slim-bookworm
WORKDIR /app

COPY --from=builder /app /app
COPY . /app/

ENV PATH="/app/.venv/bin/:$PATH"
CMD ["python", "-m", "maestro"]
