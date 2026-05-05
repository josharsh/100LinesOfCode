# Wikipedia Summary CLI

A colorful terminal tool to search and summarize any Wikipedia topic — under 100 lines of Python.

## Features

- Search any topic directly from the terminal
- Colorized output with article title, summary, and URL
- Handles disambiguation (multiple matches) interactively
- Adjustable summary length (`lines N` command)
- Supports inline CLI args: `python wiki_summary.py black holes`

## Installation

```bash
pip install wikipedia
```

## Usage

**Interactive mode:**

```bash
python wiki_summary.py
```

**Inline mode:**

```bash
python wiki_summary.py Alan Turing
python wiki_summary.py quantum computing
```

**Commands inside the prompt:**

|Command        |Action                       |
|---------------|-----------------------------|
|`lines 5`      |Change summary to 5 sentences|
|`quit` / `exit`|Exit the program             |

## Example Output

```
>>> Alan Turing
Alan Mathison Turing was an English mathematician, computer scientist, and
logician. He is widely considered to be the father of theoretical computer
science and artificial intelligence...

Read more: https://en.wikipedia.org/wiki/Alan_Turing
```

## Tech Stack

- Python 3.x
- `wikipedia` library (wraps the Wikipedia API)
- ANSI escape codes for terminal colors (no extra deps)

## Contributing

Part of the [100LinesOfCode](https://github.com/josharsh/100LinesOfCode) project.
