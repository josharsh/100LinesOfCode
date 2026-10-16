/* httpstat-mini: TCP connect / TTFB / total time for an HTTP GET.
 * build: cc -O2 -o httpstat-mini main.c
 * usage: ./httpstat-mini example.com [/path]
 */
#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <unistd.h>

static double now_ms(void)
{
    struct timeval tv;
    gettimeofday(&tv, 0);
    return tv.tv_sec * 1000.0 + tv.tv_usec / 1000.0;
}

int main(int argc, char **argv)
{
    if (argc < 2) { fprintf(stderr, "usage: %s <host> [path]\n", argv[0]); return 1; }
    const char *host = argv[1], *path = argc > 2 ? argv[2] : "/";

    struct addrinfo hints = {0}, *res;
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    if (getaddrinfo(host, "80", &hints, &res) || !res) {
        fprintf(stderr, "dns: cannot resolve %s\n", host);
        return 1;
    }
    char ip[64] = "unknown";
    struct sockaddr_in *sa = (struct sockaddr_in *)res->ai_addr;
    inet_ntop(AF_INET, &sa->sin_addr, ip, sizeof ip);

    int fd = socket(res->ai_family, res->ai_socktype, 0);
    if (fd < 0) { perror("socket"); return 1; }

    double t0 = now_ms();
    if (connect(fd, res->ai_addr, res->ai_addrlen) < 0) {
        perror("connect"); return 1;
    }
    double t_conn = now_ms() - t0;

    char req[512];
    int n = snprintf(req, sizeof req,
                     "GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: httpstat-mini\r\n"
                     "Connection: close\r\nAccept: */*\r\n\r\n", path, host);
    if (write(fd, req, n) != n) { perror("write"); return 1; }

    double t_ttfb = -1;
    long long bytes = 0;
    char buf[8192];
    for (;;) {
        ssize_t r = read(fd, buf, sizeof buf);
        if (r <= 0) break;
        if (t_ttfb < 0) t_ttfb = now_ms() - t0;
        bytes += r;
    }
    double t_total = now_ms() - t0;
    close(fd);
    freeaddrinfo(res);

    printf("  DNS+IP    : %s\n", ip);
    printf("  TCP conn  : %8.1f ms\n", t_conn);
    printf("  TTFB      : %8.1f ms\n", t_ttfb);
    printf("  total     : %8.1f ms\n", t_total);
    printf("  downloaded: %lld bytes (%.1f KB/s)\n", bytes,
           bytes / 1024.0 / (t_total / 1000.0));
    return 0;
}
