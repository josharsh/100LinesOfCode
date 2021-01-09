# Guess the Number
Author: Robert Miles

The classic "high or low" guessing game in ~~15~~ 6 lines of Python 3.8.

`guess.py` is the 6 line version, with an entire function declaration turned into an AST tree to save lines at the expense of space (and backwards compatibility past Python 3.6). If you want to actually read the source code, then you need to read `guess_unscrewed.py`, which has the function declaration written out and is 353 bytes (compared to 2041 for the "screwed" version).
