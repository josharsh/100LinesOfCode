# File server through HTTP
---

Share files through HTTP with this simple file server.

Just run the program on any folder you wish to share and the server will list for all clients the available files on your directory. You can choose ports by changing the `const int port;` variable (first line of the main function).

Only works on **linux** though because of the C libraries that were used

## Compiling

There is **no dependencies** (just `gcc 10` or newer)

```
g++ -o fshare --std=c++20 -lpthread src/main.cpp
```

### Author

[João Fukuda](https://github.com/JoaoFukuda)

