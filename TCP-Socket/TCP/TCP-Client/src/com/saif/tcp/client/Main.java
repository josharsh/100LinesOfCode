package com.saif.tcp.client;

/*
  A simple TCP client socket that connects to a server running on localhost:5000
  The client reads an input from the terminal and sends it to the server
  The server then echoes the input back to the client
  Client closes the connection if the input string is exit or the socket times out after 5 seconds
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketTimeoutException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try (Socket socket = new Socket("localhost", 5000)) {
            socket.setSoTimeout(5000); // 5 seconds
            BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
            String toServer;
            do {
                System.out.println("Enter string: ");
                toServer = scanner.nextLine();
                output.println(toServer);
                if (!toServer.toLowerCase().equals("exit")) {
                    String fromServer = input.readLine();
                    System.out.println(fromServer);
                }
            } while (!toServer.toLowerCase().equals("exit"));

        } catch (SocketTimeoutException s) {
            System.out.println("The socket timed out");
        } catch (IOException e) {
            System.out.println("Client Error: " + e.getMessage());
        }
    }
}
