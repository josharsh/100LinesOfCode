# Multi-threading using Java
Few examples of implementing multi-threading in Java. The output may vary for different operating systems and depends on how the corresponding OS schedules the threads.

## Packages Used
```bash
java.util.concurrent
java.net
```

## Multi-Threading
Synchronized concurrent thread-safe transactions are executed by different threads on the same object. This example demonstrates the different ways in which multiple threads can be synchronized such as,

* Making methods of the class `synchronized`
* Using a `sychronization` block
* Using a `Re-entrant` lock
* Using a `Re-entrant` lock with `tryLock()` method


## Multi-threading in Networking
A simple example of multi-threading in `TCP client-server` socket model. The `client` connects to the `server` and each `client` is handled on a new thread. The `server` echoes the message to the `client`. Due to multi-threading, none of the clients are blocked by each other and `client` closes the connection upon `exit` or 5 second `time-out`.
