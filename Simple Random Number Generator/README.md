# About

Author: KnochenMarkSaege

Simple Random Number Generator, written in C++ (Range-Based).\
The programm will ask you for three inputs: minimum number (inclusive), maxmimum number (inclusive) and # of times to roll.\
After you enter the three parameters, it will generate a random number in between the set Range (with time as seed)for the set # of times and outputs it inside the console.

## Additional Info

The Program uses the system built-in random generator rand() and uses the PC time\
as a seed for the random number generation.

## How to run

On Linux (or WSL for Windows): Simply open the Terminal in the Folder of the program and type:

To run the program: **./srng**\
or\
To compile & run with the clang++ compiler: **clang++ rng.cpp -o srng && ./srng**
