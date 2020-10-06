# LANComm, a simple chat application developed entirely in Python using socketserver.
# Developed by Kevin K Biju, 2020

import os
import sys
import socket
import socketserver
import json
import datetime
import threading
import hashlib

def port_input(display):
    # Ports less than 1024 are privileged and greater than 65536 are invalid so ensure correct port is given.
    while True:
        try:
            temp = int(input(display))
            break
        except ValueError:
            print("Port number must be an integer.")
            continue    
    if (temp <= 1024) or (temp > 65535):
        print("Invalid port number. Port number needs to be between 1025 and 65335")
        return port_input(display)
    return temp    
        

chat_name = input("Enter chat name: ")
send_port = port_input("Port to send on: ")
recv_address = input("Destination address: ")
recv_port = port_input("Destination port: ")
hash_salt = input("Authentication password : ")
hash_salt = hash_salt.encode()

class ChatHandler(socketserver.BaseRequestHandler):
    def handle(self):
        recv_data = json.loads(self.request.recv(1024))        
        if hashlib.blake2b(recv_data[2].encode(), salt=hash_salt).hexdigest() == recv_data[3]:
            sys.stdout.write("\r")
            sys.stdout.flush()
            print("[", recv_data[1], "at", recv_data[0], "]: ", recv_data[2])
            sys.stdout.flush()
            print("[", chat_name, "]: ", end=" ")
            sys.stdout.flush()            
        if hashlib.blake2b(recv_data[2].encode(), salt=hash_salt).hexdigest() != recv_data[3]:
            sys.stdout.write("\r")
            sys.stdout.flush()            
            print("[", recv_data[1], " at ", recv_data[0], "]: <message discarded due to integrity or authentication failure>")
            sys.stdout.flush()            
            print("[", chat_name, "]: ", end=" ")
            sys.stdout.flush() 

def screen_clear():
    if os.name == 'posix':
        return_value = os.system('clear')
    if os.name == 'nt':
        return_value = os.system('cls')
        
def client_code():
    print("[", chat_name, "]: ", end=" ")
    try:
        message = input('')
    except KeyboardInterrupt:
        print("Goodbye!")
        exit(0)
    pipe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_data = [datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"), chat_name, message, hashlib.blake2b(message.encode(), salt=hash_salt).hexdigest()]
    while True:    
        try:
            pipe.connect((recv_address, recv_port))
            pipe.send((json.dumps(send_data)).encode())
            pipe.close()
            break
        except (ConnectionRefusedError, ConnectionResetError, ConnectionAbortedError, ConnectionError) as error:
            print(error, "Retry? (Y/N)", end = '')
            if (input('').upper() == 'Y'):
                continue
            print("Message was not sent.") 
            break

print("Starting server...")
server = socketserver.TCPServer(('0.0.0.0', send_port), ChatHandler)
server_spawn = threading.Thread(target=server.serve_forever)
server_spawn.setDaemon(True)
server_spawn.start()
screen_clear()
while True:
    client_code()                          