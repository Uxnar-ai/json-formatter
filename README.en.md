# jsonfmt — paste JSON, get it formatted

> Paste JSON and get it formatted. Minify, locate syntax errors down to line and column, sort keys — all computed in your browser.

English | [中文](README.md)

## What it is

A wall of JSON from an API becomes something readable the moment you paste it.

There is no backend logic: the page is an empty shell and parsing, formatting and highlighting all run in the browser, so nothing is ever uploaded. Formatting fires 220ms after you stop typing, or on `Ctrl/⌘ + Enter`.

When parsing fails, the character offset from `JSON.parse` is converted into a line and column — far more useful than a bare `Unexpected token`. Highlighting is a single token scan, so digits inside strings are not mistaken for numbers. Key sorting is recursive; array order never changes.

## Features

- Formats as you paste, 220ms debounce, no button needed
- Syntax errors reported as line and column
- Indent 2 / 4 spaces or Tab
- Recursive key sorting that leaves arrays in order
- Minify, copy result, one-click clear
- Auto light/dark plus manual toggle; two columns above 900px

## Stack

Python 3.12 · Flask 3.1 · 原生 JS

## Run

```bash
pip install -r requirements.txt
python app.py  # 默认 127.0.0.1:8870
```

## About

Part of the **auto-lab** series — small projects written, deployed and maintained automatically by [Nix](https://github.com/Uxnar-ai) on a self-hosted server.

Placeholders such as `<SERVER_IP>` and `<LOCAL_PATH>` are sanitised values applied at publish time. This repository contains no credentials, internal addresses or personal data.

## License

MIT
