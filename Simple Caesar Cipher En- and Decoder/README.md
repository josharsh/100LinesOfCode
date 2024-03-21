# About

Author: KnochenMarkSaege

This Program is a modified version of the famous "Caesar's Cipher", where every letter in a sentence\
get's shifted by 2 characters.

With this program, you can encode & decode text in four simple steps.

## How to run

On Linux (or Windows with WSL): Open the terminal inside the folder, and type this command:\
`clang++ caesar\ cipher.cpp -o cc && ./cc` \
to compile & run the program with the clang++ compiler.

If you want to exit the program before you're finished, press:\
`Ctrl + Z`\
to terminate the program, or just close the terminal if you don't want to use it anymore.

After compiling it once with the `clang++ command`
you can run the program again by typing\
`./cc` \
inside the terminal window.

## How to use

**Note: you can input any .txt file for encoding & decoding, except the cc.txt file**\
If you want to restart the program, hit `Ctrl + Z` and type `./cc` if you already compiled the program once.

Step 1 : Choose the shift modifier (How much the letters get shifted in one direction).\
It has to be a number between 1 and 25.

Step 2: Choose if you want to `[encode]` the text, by typing `1` and hitting `enter`.\
Or if you want to `[decode]` the text, by tping `2` and hitting `enter`.

Step 3: Type `1` if you want to read in a file, or type `2` if you want to enter the text yourself, and hit `enter`.\
If you chose `1`, enter the name of the file without the extension at the end (it needs to be inside the folder), for example:\
**test**  

Step 4: Your text will now be output to a file inside the folder called **cc.txt**.
You're done! Now your message is encoded / decoded :)

## Example

Open the terminal inside the program folder. Then type:\
`clang++ caesar\ cipher.cpp -o cc && ./cc`\
Then type `3`, hit `enter`\
Type `1`, hit `enter`\
Type `1`, hit `enter`\
Type `test`, hit `enter`\
The Program now encoded the Text from test test.txt file and output the encoded text\
into the cc.txt file in the same folder.

## What is different from the original?

It works pretty much like the original, except that you can choose by how much you shift the characters.

