# httpstat-mini

A 71-line C utility that breaks down where time goes for a plain HTTP request:
DNS resolution (reported IP), TCP connect, time-to-first-byte, total time and
downloaded size/throughput. No dependencies beyond libc.

```
$ cc -O2 -o httpstat-mini main.c
$ ./httpstat-mini example.com /
  DNS+IP    : 104.20.23.154
  TCP conn  :      4.8 ms
  TTFB      :     25.8 ms
  total     :     26.4 ms
  downloaded: 932 bytes (34.5 KB/s)
```

Great for a first look at `getaddrinfo`, non-TLS sockets and microsecond
timing with `gettimeofday`. httpsonly sites will still answer on port 80
with a redirect, which is itself informative.
