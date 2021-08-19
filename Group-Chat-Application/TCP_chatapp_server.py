import socket
import threading
from datetime import datetime

HOST='127.0.0.1'
PORT= 9090

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()# start listening for TCP connections made to this socket

clients=[]#stores all clients
names=[]#stores all names of clients

def broadcast(message):#this function forwards every message to all clients
    for client in clients:
        client.send(message)

def book(client):#This function is called in a different thread for every client after handshaking ,handles client for communicating.
    while True:
        try:
            message=client.recv(1024)
            #print(f"{names[clients.index(client)]} says {message}")
            broadcast(message)
        except:#THis exception will happen when a client closes its application(socket).
            index=clients.index(client)
            clients.remove(clients[index])
            name=names[index]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            broadcast(f"SERVER: {name} lost the server at {current_time}!. MEMBER COUNT:{len(clients)}\n".encode('utf-8'))
            names.remove(name)
            break
def receive():#This function receives connection requests and put every client in a different thread.
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        client,address=server.accept()
        clients.append(client)
        print(f"Connected with {str(address)}!")
        temp="SERVER_CHECK"
        client.send(temp.encode('utf-8'))
        name=client.recv(1024)

        print(f"SERVER : {name} joined the server at {current_time}!. MEMBER COUNT:{len(clients)}\n".encode('utf-8'))
        broadcast(f"SERVER : {name} joined the server at {current_time}!. MEMBER COUNT:{len(clients)}\n".encode('utf-8'))

        thread=threading.Thread(target=book,args=(client,))#Handle every client in different thread.
        thread.start()
print("Server Running......")
receive()
