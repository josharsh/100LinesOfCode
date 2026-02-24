# Root-finding algorithm in Java

The Root class has a method calculate which takes in a lambda expression and attempts to find an input where the lambda expression returns zero using the bisection root-finding method.
The lambda expression is wrapped in an interface called Function and must take a double and return a double.
The calculate method requires a lower and upper bound to search. If no zero is found the method returns null.

## How to build and run test class

* ```javac src/*.java -d bin```
* ```java -cp bin Test```
