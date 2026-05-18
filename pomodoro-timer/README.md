# Pomodoro Timer

A CLI-based productivity tool that implements the Pomodoro Technique for effective time management.

## What is the Pomodoro Technique?

The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer Cirillo used as a university student.

## How It Works

1. Choose a task to work on
2. Set the timer for 25 minutes (one pomodoro)
3. Work on the task until the timer rings
4. Take a short 5-minute break
5. After every 4 pomodoros, take a longer 15-minute break
6. Repeat the cycle

## Features

- Configurable work and break durations
- Automatic session counting
- Long break after every 4 work sessions
- Clean CLI display with countdown timer
- Graceful exit with session summary on Ctrl+C

## Usage

Run the timer with default settings (25 min work, 5 min short break, 15 min long break):

```bash
python pomodoro_timer.py
```

Customize the durations:

```bash
python pomodoro_timer.py --work 30 --short-break 10 --long-break 20
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library modules)

## Implementation Details

This implementation uses Python's built-in `argparse` module for command-line argument parsing, `time.sleep()` for the countdown mechanism, and carriage return (`\r`) for inline timer display updates. The timer runs in an infinite loop until interrupted by the user with Ctrl+C, at which point it displays a summary of completed sessions.
