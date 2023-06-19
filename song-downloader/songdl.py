import innertube
import yt_dlp
import sys
import os
from pathlib import Path


DOWNLOAD_DIR = Path(
    os.getenv("MUSIC_DIR") or 
    os.getenv("XDG_MUSIC_DIR") or
    "~/Music"
    ).expanduser()
TEMP_DIR = Path('tmp_downloads')


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python songdl.py song1 song2 ...")

    song_ids = [ search_song(q)[0] for q in sys.argv[1:] ]
    download_song(song_ids)
    move_songs()
    

def search_song(query: str) -> list[str]:
    """Searches for a song, and returns list of matcing youtube video ids"""
    client = innertube.InnerTube("WEB")
    data = client.search(query)
    contents = (data['contents']['twoColumnSearchResultsRenderer']\
            ['primaryContents'] ['sectionListRenderer']['contents'][0]\
            ['itemSectionRenderer']['contents'])
    ids = []
    for i in range(len(contents)):
        try:
            videoContent = contents[i]["videoRenderer"]
            ids.append(videoContent["videoId"])
        except KeyError:
            continue
    return ids


def download_song(ids: list[str]) -> None:
    """Downloads songs as mp3 from youtube link using yt-dlp"""
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': {
            'default': f'{TEMP_DIR}/%(title)s.%(ext)s',
        },
        'postprocessors': [{  # Extract audio using ffmpeg
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
         }]
    }
    base_url = "https://www.youtube.com/watch?v="
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for id in ids:
            error_code = ydl.download(f"{base_url}{id}")


def move_songs() -> None:
    if not DOWNLOAD_DIR.exists():
        DOWNLOAD_DIR.mkdir()

    print(f"Moving files to {DOWNLOAD_DIR}...")
    for song in TEMP_DIR.iterdir():
        song.rename(DOWNLOAD_DIR / song.name)


if __name__ == "__main__":
    main()
