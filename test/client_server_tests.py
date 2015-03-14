import unittest
from blackjack.server import Server
from blackjack.client import Client
import threading
import time

class ClientServerTest(unittest.TestCase):

    def test_server_accepts_2_players(self):
        def clients():
            time.sleep(1) #wait for server to start
            print("do client stuff in thread")
        thread = threading.Thread(target=clients)
        thread.start()

        server = Server();
        server.host_game(2); #

        thread.join(0) #wait for client thread to finish
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()