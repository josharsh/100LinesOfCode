import sys
import time
import re

def parse_duration(time_str):
    """Parses a time string and returns the duration in seconds."""
    time_str = time_str.strip().lower()
    
    # Format: MM:SS
    if ':' in time_str:
        parts = time_str.split(':')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            return int(parts[0]) * 60 + int(parts[1])
            
    # Format: shorthand like 5m, 45s, 1h
    match = re.match(r'^(\d+)([hms])$', time_str)
    if match:
        val, unit = int(match.group(1)), match.group(2)
        if unit == 'h': return val * 3600
        if unit == 'm': return val * 60
        if unit == 's': return val
        
    # Format: Pure seconds
    if time_str.isdigit():
        return int(time_str)
        
    raise ValueError(f"Invalid time format: '{time_str}'. Try '120', '2:00', or '5m'.")

def countdown(seconds):
    """Displays a live countdown timer."""
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            
            if hours > 0:
                time_format = f"{hours:02d}:{mins:02d}:{secs:02d}"
            else:
                time_format = f"{mins:02d}:{secs:02d}"
                
            # \r returns to the start of the line to overwrite it
            print(f"\rTime remaining: {time_format}   ", end="", flush=True)
            time.sleep(1)
            seconds -= 1
            
        # Clear the line and print completion message
        print("\r" + " " * 40 + "\rTime's up!\a")
    except KeyboardInterrupt:
        print("\n\nTimer stopped by user.")
        sys.exit(0)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <duration>")
        print("Examples:")
        print("  python main.py 120    # 120 seconds")
        print("  python main.py 2:30   # 2 minutes 30 seconds")
        print("  python main.py 5m     # 5 minutes")
        sys.exit(1)
        
    try:
        duration = parse_duration(sys.argv[1])
        print(f"Starting timer for {duration} seconds...")
        countdown(duration)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
