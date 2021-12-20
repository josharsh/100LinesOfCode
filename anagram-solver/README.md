# Anagram Solver with Spellcheck!

This is a simple tool for a command line anagram solver. You can choose to print out anagrams of any subset of letters in the word by specifying the minimum length of required ``anagrams''.

#### Dependencies
```
pip3 install editdistance
pip3 install english-words
```
#### Usage
#####Run
```
./anagrams.py --no_proper_nouns --correct_spelling
```
Optional arguments:

--no_proper_nouns : If you would like to avoid proper nouns in the anagram list. If correct_spelling is set, proper nouns will also not be considered as corrections.

--correct_spelling : Will correct spelling errors in input words

Running the above will prompt the user for input words until they choose to quit.

#####Example Usage
```
ENTER WORDS TO BE ANAGRAMMED IN THE FOLLOWING FORMAT:
        ``WORD'' ``MIN_LENGTH_OF_ANAGRAM''(OPTIONAL)
ENTER ``QUIT'' TO QUIT

silent 5
ANAGRAMS OF LENGTH 5:
stile, islet
stein, inset
inlet
ANAGRAMS OF LENGTH 6:
silent, listen, tinsel



quit

```
