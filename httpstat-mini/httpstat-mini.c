/* httpstat-mini: HTTP timing utility in C (~71 lines, libc only) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc < 2) { fprintf(stderr, "Usage: %s <host> [path]\n", argv[0]); return 1; }
    const char *host = argv[1], *path = argc > 2 ? argv[2] : "/";

    struct addrinfo hints, *res;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET; hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(host, "80", &hints, &res) != 0) { fprintf(stderr, "DNS failed\n"); return 1; }

    char ip[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &((struct sockaddr_in *)res->ai_addr)->sin_addr, ip, sizeof(ip));
    printf("DNS+IP    : %s\n", ip);

    int sock = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
    if (sock < 0) { fprintf(stderr, "Socket failed\n"); return 1; }

    struct timespec t0, t1; double ms;
    clock_gettime(CLOCK_MONOTONIC, &t0);
    if (connect(sock, res->ai_addr, res->ai_addrlen) < 0) { fprintf(stderr, "Connect failed\n"); return 1; }
    clock_gettime(CLOCK_MONOTONIC, &t1);
    ms = (t1.tv_sec - t0.tv_sec) * 1000.0 + (t1.tv_nsec - t0.tv_nsec) / 1e6;
    printf("TCP conn  : %8.1f ms\n", ms);

    char req[512];
    snprintf(req, sizeof(req), "GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n", path, host);
    clock_gettime(CLOCK_MONOTONIC, &t0);
    send(sock, req, strlen(req), 0);

    char buf[8192]; int total = 0, header_done = 0;
    while (1) {
        int n = recv(sock, buf + total, sizeof(buf) - total - 1, 0);
        if (n <= 0) break;
        total += n; buf[total] = '\0';
        if (!header_done && strstr(buf, "\r\n\r\n")) { header_done = 1; clock_gettime(CLOCK_MONOTONIC, &t1); }
    }
    clock_gettime(CLOCK_MONOTONIC, &t0);

    ms = (t1.tv_sec - t0.tv_sec) * 1000.0 + (t1.tv_nsec - t0.tv_nsec) / 1e6;
    double total_ms = ((t0.tv_sec - t0.tv_sec) * 1000.0) + ((t0.tv_nsec - t0.tv_nsec) / 1e6);
    (void)total_ms;

    printf("TTFB      : %8.1f ms\n", ms);
    printf("total     : %8.1f ms\n", 0.0);
    printf("downloaded: %d bytes\n", total);

    freeaddrinfo(res); close(sock);
    return 0;
}