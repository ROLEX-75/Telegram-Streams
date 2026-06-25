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

---

## 📺 Adding the Addon to Stremio

1. Open **Stremio** → **Add-ons** tab.
2. Click the 🔍 search / URL icon.
3. Paste your manifest URL:

```
https://<your-domain>/stremio/<token>/manifest.json
```

Then go to **Settings** (`/admin/settings`).

> 🚨 **Do this first:** change the admin password in the **Admin Authentication** card, then click **Save Settings**.

Everything below is stored in the database and applied **instantly — no restart needed** (the only exception is `USER_SESSION_STRING`, which lives in `config.env`).

### ⚙️ General
| Option | What it does |
| :--- | :--- |
| **Replace Mode** | When a new file has the same quality (`720p`, `1080p`…) as an existing one, it replaces the old entry. Recommended **ON**. |
| **Hide Catalog** | Hides the public Stremio catalog (direct streams still work). |

### 🛡️ Admin Authentication
| Field | What to enter |
| :--- | :--- |
| **Admin Username / Password** | Your Web Panel login. Leave the password blank to keep the current one. **Change the defaults right away.** |
| **AUTH_CHANNELS** | The channel(s) the bot indexes and streams from. Add each one by `@username` or `-100…` ID. Make sure your bot is an **admin** in each channel. |

### 🎬 Media & Content
| Field | What to enter |
| :--- | :--- |
| **TMDB API Key** | A free TMDB **v3** key from themoviedb.org → Settings → API. Powers automatic metadata matching. |
| **Base URL** | Your public address, e.g. `https://your-domain.com`. **Important:** Stremio uses this to reach your streams. |
| **Upstream Repo / Branch** | Optional — used by `/restart` to auto-update (e.g. repo `weebzone/Telegram-Stremio`, branch `master`). |

### 💳 Subscription (optional)
Turn this on to monetise access. Set the **Subscription Group ID**, **Payment Instructions** (your UPI / bank / PayPal text), an optional **Payment QR image URL**, and the **Approver IDs** (who can approve requests). Renewal and "join the channel" prompts shown in Stremio point users back to **your bot automatically** — no separate URL to configure. The full flow is described in [Subscription Management](#-subscription-management).

### 🌐 Global Search (optional)
Requires `USER_SESSION_STRING` in `config.env` plus one app restart to unlock. Then enable the toggle and add the **channel IDs** to search. Results that aren’t in your local catalog are tagged **🌐 GLOBAL** in Stremio.

### 🌐 Proxy (optional)
Set an **HTTP Proxy URL** for outbound metadata/API requests, and optionally **show both** proxied and direct stream links.

### 🗄️ Extra Storage Databases
Your first two databases (from `config.env`) are **locked** as *Tracking* and *Storage 1*. Add more MongoDB URIs here to expand storage capacity — 🟢 means connected. Remove entries only from the **end** of the list, since existing media reference databases by position.

### 📨 Multi-Token Clients
Add extra **bot tokens** for faster parallel streaming under heavy load. Create more bots with @BotFather, add them as **admins** in all your AUTH channels, then paste their tokens here. Changes apply immediately.

> ✅ Click **Save Settings** when you’re done. That’s it — you’re live!

---

# 💳 Subscription Management

The Subscription Management system allows you to **monetise access** to your Telegram Stremio server. When enabled, users must have an active subscription to stream content.

## 📋 Subscription Plans

Admins can create and manage subscription plans from the **Admin Panel → Subscription Management** page.

Each plan has:
- **Name** (e.g. `Monthly`, `Quarterly`)
- **Duration** in days
- **Price** (for display)
- **Description**

Plans are stored in MongoDB and can be added, edited, or deleted at any time without restarting.

---

## 🤖 Bot Payment Flow

Users interact with the bot to subscribe:

```
User → /start → selects plan → sends payment screenshot
      → Approver gets notification → Approve / Reject
      → On Approve:
          ✅ Subscription saved to DB
          🔑 Stremio addon token auto-generated
          📨 User receives Stremio install link + group invite
```

**Approver actions** (available to `APPROVER_IDS`):

| Button | Action |
| :--- | :--- |
| ✅ Approve | Activates subscription, generates addon token, invites user to group |
| ❌ Reject | Notifies user with rejection message |

---

## 🗃️ Access Management

The **Admin Panel → Access Management** page gives admins full control over all users and their addon tokens.

### Columns Shown

| Column | Description |
| :--- | :--- |
| Status | 🟢 Active / 🔴 Expired |
| User | Display name or `User {id}` |
| Addon Link | Stremio install URL + copy button |
| Created | Token creation date |
| Expires | Subscription expiry date |
| Actions | Buttons for managing the user |

### Action Buttons

| Button | Description |
| :--- | :--- |
| 📅 **Assign** | Assign or extend a subscription plan (adds days) |
| ➕ **Extend** | Add extra days to an active subscription |
| ➖ **Reduce** | Subtract days from an active subscription |
| 🚫 **Revoke** | Wipe subscription entirely (marks expired) |
| 🗑️ **Del Token** | Delete the addon token only (user still subscribed) |
| 🔗 **Link User ID** | Link an old/orphan token to a Telegram user ID to enable management |

> 💡 Manually created (old) tokens that have no linked user ID show a **🔗 Link User ID** button. Once linked, all action buttons become available.

### Search & Filtering

- 🔍 Search by user name or ID
- Filter by status: All / Active / Expired
- Pagination with configurable page size

---

## 🎬 Stremio Addon Integration

### Per-User Addon Token

Each user gets a **unique addon token** automatically generated on payment approval. Their Stremio addon URL is:

```
https://your-domain.com/stremio/{token}/manifest.json
```

### Dynamic Manifest

The addon manifest updates dynamically per user:

| Scenario | Addon Name | Description |
| :--- | :--- | :--- |
| Active, has expiry | `Telegram — Expires 28 Mar 2026` | 📅 Subscription active until 28 Mar 2026 |
| Active, no expiry | `Telegram — Active` | ✅ Subscription active |
| Default (no subscription mode) | `Telegram` | Standard description |

The manifest `version` encodes the expiry date — when an admin extends or revokes a subscription, the version changes and Stremio detects an update.

### Subscription Stream Gating

When the subscription feature is enabled, the addon checks every stream request and shows a single actionable entry instead of the streams when the user isn't eligible. In both cases the stream link opens **your bot** (derived automatically from the bot's username — there is no URL to configure).

**Plan expired** — the user's subscription has lapsed:

```json
{
  "name": "🚫 Plan Expired",
  "title": "Your plan is expired.\nRenew it from the bot to continue watching.",
  "url": "https://t.me/your_bot"
}
```

**Not joined** — the user is active but has left / never joined the subscription channel (the `Subscription Group ID`):

```json
{
  "name": "📢 Join Required",
  "title": "First join the channel to stream it.\nTap here to open the bot and join.",
  "url": "https://t.me/your_bot"
}
```

Clicking the stream name opens the bot directly so the user can renew or rejoin. The membership check fails open — if Telegram is briefly unreachable or the bot can't read the group, legitimate users are never blocked.

### Configure & Reinstall Page

Every addon has a **Configure page** at:

```
https://your-domain.com/stremio/{token}/configure
```

This page shows:
- User name, subscription status, expiry date
- **⚡ Install / Update in Stremio** button (Stremio Web install flow)
- Manual install steps + **📋 Copy URL** button

The ⚙️ gear icon in Stremio opens this page so users can reinstall after an admin updates their subscription.

---

# 🚀 Deployment Guide

This guide will help you deploy your **Telegram Stremio Media Server** using either Heroku or a VPS with Docker.

## ✅ Recommended Prerequisites

**Supported Servers:**

  - 🟣 **Heroku**
  - 🟢 **VPS** 

Before you begin, ensure you have:

1.  ✅ A **VPS** with a public IP (e.g., Ubuntu on DigitalOcean, AWS, Vultr, etc.)
2.  ✅ A **Domain name**


## 🐙 Heroku Guide

Follow the instructions provided in the Google Colab Tool to deploy on Heroku.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/weebzone/Colab-Tools/blob/main/telegram%20stremio.ipynb)


## 🐳 VPS Guide

This section explains how to deploy your **Telegram Stremio Media Server** on a VPS using **Docker Compose (recommended)** or **Docker**.


### 1️⃣ Step 1: Clone & Configure the Project

```bash
git clone https://github.com/weebzone/Telegram-Stremio
cd Telegram-Stremio
mv sample_config.env config.env
nano config.env
```

* Fill in all required variables in `config.env`.
* Press `Ctrl + O`, then `Enter`, then `Ctrl + X` to save and exit.

## ⚙️ Step 2: Choose Your Deployment Method

You can deploy the server using either **Docker Compose (recommended)** or **plain Docker**.



### 🟢 **Option 1: Deploy with Docker Compose (Recommended)**

Docker Compose provides an easier and more maintainable setup, environment mounting, and restart policies.

#### 🚀 Start the Container

```bash
docker compose up -d
```

Your server will now be running at:
➡️ `http://<your-vps-ip>:8000`

---

#### 🛠️ Update `config.env` While Running

If you need to modify environment values (like `BASE_URL`, `AUTH_CHANNEL`, etc.):

1. **Edit the file:**

   ```bash
   nano config.env
   ```
2. **Save your changes:** (`Ctrl + O`, `Enter`, `Ctrl + X`)
3. **Restart the container to apply updates:**

   ```bash
   docker compose restart
   ```

⚡ Since the config file is mounted, you **don’t need to rebuild** the image — changes apply automatically on restart.



### 🔵 **Option 2: Deploy with Docker (Manual Method)**

If you prefer not to use Docker Compose, you can manually build and run the container.

#### 🧩 Build the Image

```bash
docker build -t telegram-stremio .
```

#### 🚀 Run the Container

```bash
docker run -d -p 8000:8000 telegram-stremio
```

Your server should now be running at:
➡️ `http://<your-vps-ip>:8000`



### 🌐 Step 3: Add Domain (Required)

#### 🅰️ Set Up DNS Records

Go to your domain registrar and add an **A record** pointing to your VPS IP:

| Type | Name | Value             |
| ---- | ---- | ----------------- |
| A    | @    | `195.xxx.xxx.xxx` |


#### 🧱 Install Caddy (for HTTPS + Reverse Proxy)

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
chmod o+r /usr/share/keyrings/caddy-stable-archive-keyring.gpg
chmod o+r /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

#### ⚙️ Configure Caddy

1. **Edit the Caddyfile:**

   ```bash
   sudo nano /etc/caddy/Caddyfile
   ```

2. **Replace contents with:**

   ```caddy
   your-domain.com {
       reverse_proxy localhost:8000
   }
   ```

   * Replace `your-domain.com` with your actual domain name.
   * Adjust the port if you changed it in `config.env`.

3. **Save and reload Caddy:**

   ```bash
   sudo systemctl reload caddy
   ```


✅ Your API will now be available securely at:
➡️ `https://your-domain.com`


# 📺 Setting Up Your App (Nuvio Recommended)

Your media server works as a standard **Stremio-style addon**, so it plays in any compatible client. For the **best compatibility and smoothest experience across devices, we recommend the [Nuvio](https://play.google.com/store/apps/details?id=com.nuvio.app) app** — a free, open-source media hub for **Android, Android TV, Fire TV, iOS, Windows, and TV** that supports Stremio addon manifest URLs natively. *(Content was rephrased for compliance with licensing restrictions.)*

> 💡 Already using **Stremio**? It works too — just install the same addon URL below. Nuvio simply tends to handle these Telegram streams more reliably across more devices.

## 📥 Step 1: Install Nuvio

Download Nuvio from an official source:

| Platform | Source |
| :--- | :--- |
| **Android / Android TV / Fire TV** | [Google Play](https://play.google.com/store/apps/details?id=com.nuvio.app) |
| **All platforms / latest builds** | [GitHub — tapframe/NuvioStreaming](https://github.com/tapframe/NuvioStreaming) |

> 🔗 *(Optional)* Connect **Trakt** in the app to sync your watch history and progress across devices.

## 🌐 Step 2: Add the Addon

1. Open **Nuvio** and go to the **Addons** section.
2. Paste your addon **manifest URL** and install it:

| Deployment Method | Addon URL |
| :--- | :--- |
| **Heroku** | `https://<your-heroku-app>.herokuapp.com/stremio/manifest.json` |
| **Custom Domain** | `https://<your-domain>/stremio/manifest.json` |

3. Done! 🎉 Your Telegram library now appears in the catalog and streams directly.

> 🔑 If you run in **subscription mode**, each user installs their own **personal** addon URL (`/stremio/{token}/manifest.json`) that the bot gives them.


## 🏅 Contributors

|<img width="80" src="https://avatars.githubusercontent.com/u/113664541">|<img width="80" src="https://avatars.githubusercontent.com/u/13152917">|<img width="80" src="https://avatars.githubusercontent.com/u/14957082">|<img width="80" src="https://raw.githubusercontent.com/vflixa1prime/Readme/main/VFlixPRime.png">|
|:---:|:---:|:---:|:---:|
|[`Karan`](https://github.com/Weebzone)|[`Stremio`](https://github.com/Stremio)|[`ChatGPT`](https://github.com/OPENAI)|[`VFlix Prime`](https://t.me/vflixprime2)|
|Author|Stremio SDK|Refactor|Community Support
