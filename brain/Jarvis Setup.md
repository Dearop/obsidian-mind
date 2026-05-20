---
date: 2026-04-27
description: "Jarvis (NanoClaw agent) operational setup — capabilities, credentials, scheduled tasks, and workflows for Paul"
tags:
  - brain
  - jarvis
---

# Jarvis Setup

Operational context for Jarvis, the NanoClaw AI agent running in a containerized workspace connected to Paul via Telegram (`telegram-mg-17769`).

## Identity

- **Name**: Jarvis
- **Channel**: Telegram → `telegram-mg-17769` (Paul Quesnot)
- **Workspace**: `/workspace/agent/`
- **Model**: Claude Sonnet 4.6

## Capabilities Installed

- **Voice transcription**: Local Whisper via `@huggingface/transformers` (onnx-community/whisper-base). Module: `/workspace/agent/transcribe.js`. No API key needed.
- **Google Calendar**: OAuth2 via `googleapis` npm. Module: `/workspace/agent/gcal.js`. Credentials: `/workspace/agent/gcal_credentials.json`.
- **qmd 2.1.0**: Semantic search across the obsidian-mind vault. Commands: `qmd query`, `qmd search`, `qmd vsearch`.
- **Obsidian Mind vault**: Cloned at `/workspace/agent/obsidian-mind/`. SSH key at `/workspace/agent/.ssh/id_ed25519`.
- **ffmpeg**: Installed system-wide for audio conversion.

## Scheduled Tasks

### Daily Morning Briefing (`task-1776970858045-66c6tq`)
- **Schedule**: Every day at 8:00 AM Zurich time
- **Content**: Today's Google Calendar events (with context) + top 2-3 stories on AI, ZK, Crypto, Geopolitics + philosophical quote of the day
- **Source**: Web search only (no X/Twitter)

### Apartment Monitor (`task-1777112557345-y0y0gr`)
- **Schedule**: Every day at 8:00 AM and 6:00 PM Zurich time
- **Criteria**: Studio or 2-room, Zurich, <1200 CHF/month, ~30 min from ETH Zentrum, available July 1–September 1 2026
- **Platform**: flatfox.ch only (homegate + immoscout blocked)
- **Dedup file**: `/workspace/agent/seen_listings.json`
- **Alert**: Only messages Paul when new listings found

## Google Calendar

- **Status**: ✅ Connected via OAuth2 (Production — token does not expire)
- **Credentials**: `/workspace/agent/gcal_credentials.json`
- **Module**: `/workspace/agent/gcal.js` — exports `createEvent`, `listUpcomingEvents`
- **Client ID**: 204049232180-98tqm87f2t3opakgp1b529aa6duvlq60.apps.googleusercontent.com
- **OAuth app**: Published to Production on 2026-05-20. Desktop app type. Redirect URI: `http://localhost`.

## Vault Git Access

- **Repo**: `git@github.com:Dearop/obsidian-mind.git`
- **SSH key**: `/workspace/agent/.ssh/id_ed25519` (stored in persistent workspace — survives container rebuilds)
- **Git config**: Uses `core.sshCommand` pointing to workspace key

## Laptop Context (NanoClaw host)

- **Machine**: System76 laptop running Pop!_OS
- **Issue**: Lid close causes overheating — ACPI handler created to switch to Battery power profile on lid close
- **AMD interrupt flood**: AMDI0010:03 at 433/s — fix: `echo "on" > /sys/bus/platform/devices/AMDI0010:03/power/control` (not confirmed applied)
- **ACPI files**: `/etc/acpi/events/lid-thermal` + `/etc/acpi/actions/lid-thermal.sh`

## Related

- [[Paul Profile]]
- [[North Star]]
- [[Memories]]
