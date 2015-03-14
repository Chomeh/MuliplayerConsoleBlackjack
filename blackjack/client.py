class Client():

    def __init__(self,server):
        #create connection
        print("Codemeplease")

    def join_game(self):
        print("Codemeplease")

    #return 2 cards
    #call after get game state indicates server is ready.
    def bet(self,bet):
        print("CodeMePlease.")

    #server responds with this game state
    #and whether it requires a decision from the client.
    def get_game_state(self):
        print("CodeMePlease.")

    #call after game state, indicates server is ready.
    #Choise is to draw or pass, repeats until the end of the game.
    #should return the state of the game.
    #Server may reject and ask again.
    def play_round(self, choice):
        print("CodeMePlease.")