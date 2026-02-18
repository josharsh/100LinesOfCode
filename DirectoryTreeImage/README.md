# Directory Tree Image Generator (Java)
* A signle file utility that visualizes your direstory structure.
* It outputs a classic tree view to the console **and** generates a dark mode PNG report and saves the image to `tree_structure.png`.
* Also, auto-calculates sizes (B/KB) for every file.
* Automatically ignores clutter like `.git`, `.idea`, `node_modules` and more. 
* Runs on Standard Java
### Note:
(You can change Line 11 in `DirectoryTreeImage.java` to include or remove accordingly to your preferences!)



# Usage
### 1. Compile 
```
javac DirectoryTreeImage.java
```
### 2. Run
The program will ask you which folder to scan. If you press Enter it will scan the current folder
```
java DirectoryTreeImage 
```
Output: 
```
Path (Enter for current):
```
Where you can provide the path you want the program to start from
### 3. Example
Here is a usage example for the Enter case (the current folder the programm is executed). The output in the console will look something like the following:
```
DirectoryTreeImage  
├── DirectoryTreeImage.class 7 KB
├── DirectoryTreeImage.java 5 KB
└── README.md 0 B
[+] Saved report to tree_structure.png
```



