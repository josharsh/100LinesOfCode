import pyaudio
import pickle
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 22000))
s.listen(1)
clientconnected,addr = s.accept()
print('connected by',addr)
import struct
BUFFER_SIZE = 1024
play=pyaudio.PyAudio()
stream_play=play.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      frames_per_buffer=CHUNK,
                      output=True)
while True:
    data = b''
    payloaf_size = struct.calcsize("Q")
    while True:
        while len(data) < payloaf_size:
            message = clientconnected.recv(BUFFER_SIZE)
            data += message
        packed_msg_size = data[:payloaf_size]
        data = data[payloaf_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        while len(data) < msg_size:
            message = clientconnected.recv(BUFFER_SIZE)
            data += message
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        print(frame)
        stream_play.write(frame[0], CHUNK)



print("* done recording")
