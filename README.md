# Aegis - The All-in-One Community Management Bot

Aegis is a modular Discord bot designed to handle a wide range of community management tasks. Each major feature resides in its own module so that the codebase stays maintainable and easy to extend.

## Philosophy

- **Maintain Modularity**: Develop new features as individual cogs under `src/modules/`.
- **Abstract Core Logic**: Place common helpers in `src/utils/` to avoid code duplication.
- **Prioritize Documentation**: Every function and class must include clear docstrings and inline comments describing its behavior.

## Getting Started

1. Clone the repository.
2. Install Python dependencies with `pip install -r requirements.txt`.
3. Configure your environment variables (bot token, database URL, etc.).
4. Add new modules under `src/modules/` and share helpers in `src/utils/`.

## Features Overview

- Dynamic voice channel management
- Server economy with virtual shop
- User leveling system
- Administrator toolkit
- Music playback
- Web dashboard (Next.js) for server configuration

This repository currently provides the project skeleton. Future contributions are welcome!

## Web Dashboard

The `dashboard/` directory contains a minimal Next.js application used for
future configuration of the bot via a web interface. To get started:

```bash
cd dashboard
npm install
npm run dev
```

This will start the Next.js development server on `http://localhost:3000`.
