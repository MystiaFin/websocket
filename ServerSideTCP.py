import socket
import sys

host = '172.25.1.162'
data_payload = 1024
backlog = 2  # Two connections for Room 1 and Room 2 players

def determine_winner(choice1, choice2):
    """Determine the winner between two choices."""
    outcomes = {
        ('Rock', 'Scissors'): 'Player 1',
        ('Scissors', 'Paper'): 'Player 1',
        ('Paper', 'Rock'): 'Player 1',
        ('Scissors', 'Rock'): 'Player 2',
        ('Paper', 'Scissors'): 'Player 2',
        ('Rock', 'Paper'): 'Player 2'
    }
    if choice1 == choice2:
        return "It's a draw!"
    return f"{outcomes.get((choice1, choice2))} won!"

def rock_paper_scissors_server(port):
    """Server for Rock-Paper-Scissors Game"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print(f"Starting server at {server_address}")
    sock.bind(server_address)
    sock.listen(backlog)

    clients = []
    while len(clients) < 2:
        print("Waiting for connections...")
        client, address = sock.accept()
        print(f"Connected to {address}")
        clients.append((client, address))

    # Receive choices
    choices = []
    for client, address in clients:
        data = client.recv(data_payload).decode()
        print(f"Received choice '{data}' from {address}")
        choices.append(data)

    # Determine winner
    result = determine_winner(choices[0], choices[1])
    print(f"Game result: {result}")

    # Send results back to clients
    for client, _ in clients:
        client.sendall(result.encode('utf-8'))
        client.close()

if __name__ == "__main__":
    port = int(input("Enter port to run the server: "))
    rock_paper_scissors_server(port)
