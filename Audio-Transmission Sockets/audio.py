"""Server for audio transmission"""

import wave
import struct
import socket
import pickle
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 22000))
s.listen(1)
clientconnected,addr = s.accept()
print('connected by',addr)
BUFFER_SIZE = 1024
play=pyaudio.PyAudio()
stream_play=play.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      frames_per_buffer=CHUNK,
                      output=True)

WAV_WRITE = False

if WAV_WRITE:
    wav_file = wave.open("output.wav", "wb")
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(play.get_sample_size(FORMAT))
    wav_file.setframerate(RATE)

while True:
    DATA = b''
    payload_size = struct.calcsize("Q")
    try:
        while True:
            while len(DATA) < payload_size:
                message = clientconnected.recv(BUFFER_SIZE)
                DATA += message
            packed_msg_size = DATA[:payload_size]
            DATA = DATA[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            while len(DATA) < msg_size:
                message = clientconnected.recv(BUFFER_SIZE)
                DATA += message
            frame_DATA = DATA[:msg_size]
            DATA = DATA[msg_size:]
            frame = pickle.loads(frame_DATA)
            print(frame)
            stream_play.write(frame[0], CHUNK)
            if WAV_WRITE:
                wav_file.writeframes(frame[0])
    except KeyboardInterrupt:
        if WAV_WRITE:
            wav_file.close()
        print("Exiting...")
        break
