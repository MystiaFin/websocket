import socket
import sys

host = 'localhost'

def rock_paper_scissors_client(port, choice):
    """Client for Rock-Paper-Scissors Game"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print(f"Connecting to server at {server_address}")
    sock.connect(server_address)
    try:
        print(f"Sending choice: {choice}")
        sock.sendall(choice.encode('utf-8'))
        data = sock.recv(1024)
        print(f"Received result: {data.decode()}")
    finally:
        print("Closing connection to server")
        sock.close()

if __name__ == "__main__":
    port = int(input("Enter server port: "))
    choice = input("Enter your choice (Rock/Paper/Scissors): ").capitalize()
    rock_paper_scissors_client(port, choice)
