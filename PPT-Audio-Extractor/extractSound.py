import sys
import os.path
import zipfile
import shutil
from pydub import AudioSegment

def main():
    fileName = sys.argv[1]
    if not os.path.isfile(fileName):
        print('File does not exist')
        return
    with zipfile.ZipFile(fileName,"r") as zip_ref:
        zip_ref.extractall("targetdir")
    audioFileNum = 1
    path = "targetdir/ppt/media/audio{}.wav".format(audioFileNum)
    if not os.path.isfile(path):
        print('No audio files in this ppt')
        return
    combinedSound = AudioSegment.from_wav(path)
    audioFileNum = audioFileNum + 1
    while os.path.isfile("targetdir/ppt/media/audio{}.wav".format(audioFileNum)):
        combinedSound = combinedSound + \
         AudioSegment.from_wav("targetdir/ppt/media/audio{}.wav".format(audioFileNum))
        audioFileNum = audioFileNum + 1
    combinedSound.export("joinedFile.wav", format="wav")
    dir_path = 'targetdir'
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
if __name__ == '__main__':
    main()

