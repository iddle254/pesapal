#!/usr/bin/python3
import socket
"""
This implementation starts a TCP server that listens on the specified host and port
and accepts up to N clients. Clients are assigned ranks based on the order they connect,
and the server distributes commands received from clients to all clients with a lower rank.
If a client disconnects, the server adjusts the ranks of the remaining clients to fill any gaps.
"""
max_clients = 10  # maximum number of clients
clients = []  # list of connected clients


def distribute_command(command, sender_rank):
    """Continuously distribute commands among clients"""
    for client in clients:
        if client["rank"] > sender_rank:
            client["socket"].send(command.encode())


def handle_client(client_socket, client_address):
    """Handles a single client connection"""
    rank = len(clients)  # assign the next available rank
    client = {"socket": client_socket, "rank": rank, "address": client_address}
    clients.append(client)
    print(f"Accepted client {client_address} with rank {rank}")
    try:
        while True:
            command = client_socket.recv(1024).decode()
            if not command:
                break  # client disconnected
            print(f"Received command '{command}' from client {client_address}")
            distribute_command(command, rank)
    finally:
        clients.remove(client)  # remove client from list
        print(f"Client {client_address} with rank {rank} disconnected")
        # promote clients to fill any gaps in the ranks
        for i in range(rank, len(clients)):
            clients[i]["rank"] -= 1


def run_server(host, port):
    """Starts the TCP server"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(max_clients)
    print(f"Server listening on {host}:{port}")
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket, client_address)
    finally:
        server_socket.close()


run_server("127.0.0.1", 46461)
