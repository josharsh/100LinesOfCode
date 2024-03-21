import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ip address', 13050))
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")
import pickle
import struct
frames = []
while True:

    data = [stream.read(CHUNK)]
    data = pickle.dumps(data)

    message_size = struct.pack("Q", len(data))
    s.sendall(message_size + data)
