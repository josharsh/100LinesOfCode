"""
Pomodoro Timer - A CLI productivity tool

Implements the Pomodoro Technique: 25-minute work sessions followed by
5-minute short breaks, with a 15-minute long break after every 4 sessions.

Usage:
    python pomodoro_timer.py [--work MINUTES] [--short-break MINUTES] [--long-break MINUTES]

Example:
    python pomodoro_timer.py --work 25 --short-break 5 --long-break 15
"""

import argparse
import sys
import time


def display_timer(seconds: int, session_type: str) -> None:
    """Display a countdown timer with session type label.

    Args:
        seconds: Remaining time in seconds.
        session_type: Label for the current session (e.g., 'Work', 'Short Break').
    """
    minutes = seconds // 60
    secs = seconds % 60
    print(f"\r  {session_type}: {minutes:02d}:{secs:02d}  ", end="", flush=True)


def countdown(duration_minutes: int, session_type: str) -> None:
    """Run a countdown timer for the specified duration.

    Args:
        duration_minutes: Length of the timer in minutes.
        session_type: Label displayed during the countdown.
    """
    total_seconds = duration_minutes * 60
    for remaining in range(total_seconds, -1, -1):
        display_timer(remaining, session_type)
        time.sleep(1)
    print()  # New line after timer completes


def run_pomodoro(work_min: int, short_break_min: int, long_break_min: int) -> None:
    """Execute the full Pomodoro Technique cycle.

    Runs 4 work sessions with short breaks in between, followed by a long break.
    After the long break, the cycle repeats indefinitely until interrupted.

    Args:
        work_min: Duration of each work session in minutes.
        short_break_min: Duration of short breaks in minutes.
        long_break_min: Duration of the long break in minutes.
    """
    session_count = 0

    print("=" * 50)
    print("  POMODORO TIMER")
    print("  Press Ctrl+C to stop at any time")
    print("=" * 50)

    try:
        while True:
            session_count += 1
            print(f"\n>>> Session {session_count} starting...")

            countdown(work_min, "Work")
            print("  Work session complete! Time for a break.")

            if session_count % 4 == 0:
                print(f"  Great job! Taking a long break ({long_break_min} min).")
                countdown(long_break_min, "Long Break")
            else:
                print(f"  Taking a short break ({short_break_min} min).")
                countdown(short_break_min, "Short Break")

            print("  Break over. Ready for the next session!")

    except KeyboardInterrupt:
        print(f"\n\nTimer stopped. Completed {session_count} session(s).")
        print("Stay productive!")
        sys.exit(0)


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for timer configuration.

    Returns:
        Parsed arguments namespace with work, short_break, and long_break values.
    """
    parser = argparse.ArgumentParser(
        description="Pomodoro Timer - Boost your productivity with timed work sessions"
    )
    parser.add_argument(
        "--work", type=int, default=25, help="Work session duration in minutes (default: 25)"
    )
    parser.add_argument(
        "--short-break", type=int, default=5, help="Short break duration in minutes (default: 5)"
    )
    parser.add_argument(
        "--long-break", type=int, default=15, help="Long break duration in minutes (default: 15)"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    run_pomodoro(args.work, args.short_break, args.long_break)
