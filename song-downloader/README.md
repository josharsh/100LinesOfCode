# Song Downloader

A simple python project that lets you download songs
from the command line.

## Requirements

* [Python](https://www.python.org/downloads/)
* [ffmpeg](https://ffmpeg.org/download.html) (For converting to mp3)

### Setup

You will need to create a virtual environment and download
dependencies for this project to work. I have included two
shell scripts for Linux/macOS and Windows systems that will
help you configure the environment automatically.

#### Windows (powershell)

```powershell
.\configure.ps1
```

#### Linux/macOS

```bash
./configure.sh
```

### Usage

```bash
python songdl.py song1 "song two" ...
```

By default the download directory is set to `$XDG_MUSIC_DIR` or `~/Music`

Use the environment variable `MUSIC_DIR` to provide a custom directory
for downloading songs.

#### Linux/macOS (dedupe heading)

```bash
export MUSIC_DIR="~/path/to/custom/dir"
```

#### Windows (powershell) (dedupe heading)

```bash
$env:MUSIC_DIR="~/path/to/custom/dir"
```

Then you can use normal download commands.

### Author

[diwasrimal](https://github.com/diwasrimal)
