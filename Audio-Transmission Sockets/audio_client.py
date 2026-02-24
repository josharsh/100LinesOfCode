"""Audio Transmission Sockets"""

import pickle
import struct
import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 22000))
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")
frames = []
while True:
    try:
        data = [stream.read(CHUNK)]
        data = pickle.dumps(data)

        message_size = struct.pack("Q", len(data))
        s.sendall(message_size + data)
    except ConnectionResetError as e:
        print(e)
        break
