# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY app.py .

# CMD ["python", "app.py"]

# ── Étape 1 : Builder ──────────────────
FROM python:3.12-slim AS builder

WORKDIR /build

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# ── Étape 2 : Runtime ──────────────────
FROM python:3.12-slim AS runtime

COPY --from=builder /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN useradd --uid 1001 --no-create-home appuser

WORKDIR /app

COPY app.py .

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]