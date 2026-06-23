FROM ghcr.io/astral-sh/uv:debian-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV LANG=en_US.UTF-8
ENV PATH="/app/.venv/bin:$PATH"

# ── Change these two to point at your GitHub repo ──────────────────────────
ARG REPO=https://github.com/ROLEX-75/Telegram-Stremio
ARG BRANCH=main
# ───────────────────────────────────────────────────────────────────────────

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        bash \
        git \
        curl \
        ca-certificates \
        locales && \
    locale-gen en_US.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Clone your project from GitHub at build time (no files needed in HF Space)
RUN git clone --depth=1 --branch ${BRANCH} ${REPO} .

RUN uv lock
RUN uv sync --locked
RUN chmod +x start.sh
CMD ["bash", "start.sh"]
