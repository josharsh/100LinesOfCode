# Pomodoro Timer (Kotlin)

A simple command-line Pomodoro timer written in Kotlin using coroutines.  
This tool lets you run configurable Pomodoro cycles directly from the terminal.

---

## Features

- Countdown timer for work and break sessions
- Configurable durations via CLI flags
- Adjustable number of cycles
- Smooth terminal-updating countdown
- No external configuration or dependencies beyond Kotlin + Gradle
- Code kept intentionally concise and beginner-friendly

---

## How to Run

Make sure you are in the project directory and the Gradle wrapper is present.

### Using Gradle (recommended)

```bash
./gradlew run --args="--work 25 --break 5 --cycles 4"
```
