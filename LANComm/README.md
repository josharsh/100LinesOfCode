# LANComm: A Simple Chat Application operation on a Client-Server Model.

This is a simple chat app built using Python's socket and socketserver modules. It should work over all LAN and internal Wi-Fi networks. Messages are sent with their hash (generated using an unknown salt), to ensure integrity and authentication.

The application operates with two different threads of execution. The first is a simple TCPServer that binds to the user-specified port and listens forever for incoming messages. After the messages is deserialized, it checks if the hash of the message sent by the client matches the hash the server generates with its own salt, if they do not match, the message is discarded.

Each message is sent as a JSON stream comprising of: client-side current system datetime, chat name, message and its corresponding hash(in hexadecimal).  

The client-side thread reads a message from the user, hashes it with the client-side salt and sends it in a JSON stream to the destination for the server to process. Each messages opens and closes a seperate socket.

Usage: On two different devices, execute on the terminal

```python3 bleh2.py```

On each device, enter a client side port to use, along with the destination server's address and port. It follows that one side's client is the other side's server and so the addresses should match accordingly. Also set a chat name to use and authentication password which is used as a hash salt. These should match on both devices or no messages will be readable.

Enjoy!
