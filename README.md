---
title: TG Stremio
emoji: 🎬
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

<p align="center">
  <img src="https://iili.io/KhN0ztj.png" alt="Logo" width="400"/>
</p>

<p align="center">
  A powerful, self-hosted <b>Telegram Stremio Media Server</b> built with <b>FastAPI</b>, <b>MongoDB</b>, and <b>PyroFork</b> — seamlessly integrated with <b>Stremio</b> for automated media streaming and discovery.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Stremio-8D3DAF?logo=stremio&logoColor=white" alt="Stremio" />
</p>

---

## ⚙️ Configuration

Copy `sample_config.env` to `config.env` and fill in the required variables:

| Variable | Description |
| :--- | :--- |
| `API_ID` | Telegram API ID from `my.telegram.org` |
| `API_HASH` | Telegram API Hash from `my.telegram.org` |
| `BOT_TOKEN` | Bot token from `@BotFather` |
| `OWNER_ID` | Your Telegram User ID |
| `DATABASE` | MongoDB URIs (comma-separated, exactly 2: tracking + storage) |
| `PORT` | FastAPI server port (default: `8000`) |
| `USER_SESSION_STRING` | Optional — required only for Global Search |

> All other settings (AUTH\_CHANNEL, TMDB\_API, proxies, subscriptions, etc.) can be managed from the **Web Admin Panel** after startup.

---

## 🚀 Deployment

### 🤗 Hugging Face Spaces (Docker)

1. Fork this repository to your GitHub account.
2. Create a new **Hugging Face Space** → choose **Docker** SDK.
3. Connect your GitHub fork.
4. Add all required variables (listed above) as **Space Secrets** under *Settings → Variables and Secrets*.
5. Set `PORT=7860` (HF Spaces exposes port 7860 by default).
6. The Space will build and start automatically.

### 🐳 VPS / Docker Compose

```bash
git clone https://github.com/weebzone/Telegram-Stremio
cd Telegram-Stremio
cp sample_config.env config.env
nano config.env          # fill in your values
docker compose up -d
```

Your server will be running at `http://<your-vps-ip>:8000`.  
Point a domain at your VPS and use a reverse proxy (Caddy / Nginx) for HTTPS.

---

## 📺 Adding the Addon to Stremio

1. Open **Stremio** → **Add-ons** tab.
2. Click the 🔍 search / URL icon.
3. Paste your manifest URL:

```
https://<your-domain>/stremio/<token>/manifest.json
```

---

## 🏅 Contributor

| <img width="80" src="https://avatars.githubusercontent.com/u/113664541"> |
|:---:|
| [`Karan`](https://github.com/Weebzone) |
| Author |
