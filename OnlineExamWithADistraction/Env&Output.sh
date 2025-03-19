Environment
export PATH="/c/Users/SUNYLoaner/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64:$PATH"
export CGO_CFLAGS="-I/c/Users/SUNYLoaner/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64/include"
export CGO_LDFLAGS="-L/c/Users/SUNYLoaner/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64/mingw_libs -lvlc -lvlccore"
export PATH="/c/Users/SUNYLoaner/Downloads/VideoLAN.LibVLC.Windows.3.0.21/build/x64/mingw_libs:$PATH"

Output
$ go build -o onlineExamWithADistraction onlineExamWithADistraction.go
$ ./onlineExamWithADistraction
2025/03/18 22:31:53 Streaming... Press Ctrl+C to stop.
[src/libmpg123/layer3.c:INT123_do_layer3():1773] error: part2_3_length (768) too large for available bit count (736)
2025/03/18 22:32:00 Interrupt received. Stopping playback.
