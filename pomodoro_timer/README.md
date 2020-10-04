# Pomodoro Timer

Throughout college, I have used the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) to effectively manage my study sessions. During my freshman year, I had this weird obsession on using just the terminal for most of my computer needs, including setting up a timer for my study-break intervals. At the time, I found that there wasn't a native unix command that will show a countdown timer and will set off an alarm when the time is up. And thus I wrote this simple script, and have used it since then. :)  

## Usage
1. Add the pomodoro script on your ~/bin directory.
2. Make sure to set the script to be executable: `$chmod +x pomodoro`
3. Since ~/bin is in your executable PATHs, you may run the script like a native command: `pomodoro <num_of_minutes>`
4. You may exit the timer anytime by sending an interrupt: ctrl+c
