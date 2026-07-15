# Countdown Timer CLI

A lightweight, terminal-based countdown timer written in under 100 lines of pure Python. Perfect for focus sessions, Pomodoro timers, or cooking!

## Features
- **No external dependencies**: Uses only the Python standard library.
- **Live Terminal Updates**: Overwrites the same line on the console for a clean, live countdown experience.
- **Flexible Input Parsing**: Understands pure seconds, `MM:SS`, and shorthand formats like `5m`, `45s`, or `1h`.
- **Audio Cue**: Emits a terminal bell sound (`\a`) when the timer finishes.
- **Graceful Interrupts**: Handles `Ctrl+C` cleanly without throwing error traces.

## Usage

Run the script from your terminal and provide the duration.

```bash
# Pure seconds (e.g. 120 seconds)
python main.py 120

# Minutes and seconds
python main.py 2:30

# Shorthand notation
python main.py 5m
python main.py 45s
python main.py 1h
```
