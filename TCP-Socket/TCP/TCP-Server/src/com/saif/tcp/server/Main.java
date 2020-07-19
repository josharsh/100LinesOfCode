package com.saif.tcp.server;
/*
  A TCP server socket.
  It accepts connections from client sockets on port 5000 and runs each connection on a new thread.
  As a result none of the clients are blocked by each other.
  The server simply echoes the message back to the clients.
*/

import java.io.IOException;
import java.net.ServerSocket;

public class Main {

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(5000)) {
            while (true) {
                new ServerThread(serverSocket.accept()).start();
            }

        } catch (IOException e) {
            System.out.println("Server Error: " + e.getMessage());
        }
    }
}
