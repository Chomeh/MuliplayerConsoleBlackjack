import socket

class Server:
    def __init__(self):
        self.players = []

    def host_game(self, number_of_players):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('localhost', 8089))
        max_queued_connections = 1
        serverSocket.listen(max_queued_connections)

        #wait for players to connect
        for i in range(1,number_of_players):
            connection, address = serverSocket.accept()
            self.players.append(PlayerClient(connection))


class PlayerClient:
    def __init__(self, connection):
        self.connection = connection
        #get player name, expect the first message is the player name
        self.name = buffer = connection.recv(64)
        print(self.name + " has joined the game")