import yt_dlp
from time import sleep
import shutil
print("Welcome to NoBloatDL!")
print("Made by Notlock")
print("")
print("Loading...")
if not shutil.which("ffmpeg"):
    print("ffmpeg is not installed. Download it at https://ffmpeg.org/download.html")
sleep(2)
print("")

## determines file type
def aorv():
    q = input("Enter 1 if you want video and audio, or 2 if you want only audio.")
    if q == "1":
        ext = "mp4"
        form = "bestvideo[vcodec^=avc1]+bestaudio/bestvideo+bestaudio/best"
    elif q == "2":
        ext = "mp3"
        form = "bestaudio/best"
        ydl_opts["postprocessors"] = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}]
    else:
        print("You entered an invalid number, please exit the program and run again.")
    return ext, form

## download proccess hook
def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rProgress: {percent} | ETA: {eta}s", end='')
    elif d['status'] == 'finished':
        print("\nDownload complete!")
    
while True:
    URL = input("Enter video Url: ")
    title = input("Enter the name of the output file: ")
    ext,form = aorv() 
    temp = f"{title}.{ext}"
    save_dir = input("Enter the directory you would like to save to: ")
    # Options dict
    ydl_opts = {
        "format": form,
        "outtmpl": f"{save_dir}/{temp}",
    }
    if ext == "mp4":
        ydl_opts["merge_output_format"] = "mp4"
    elif ext == "mp3":
        ydl_opts["postprocessors"] = [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}]
    

    # download track
    ydl_opts["progress_hooks"] = [progress_hook]

    # Download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
        
    again = input("Download another? (y/n): ")
    if again.lower() != "y":
        break