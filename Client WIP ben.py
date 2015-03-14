#Classes

import random
import socket

class BlackJackClient():
	
	def __init__(self,server):
		Host_IP = input("Please enter the host IP: ")
		Host_Port = input("Please enter the host Port: ")
		name = input("Please enter your player name: ")
		clientSocket = socket.socket(Socket.AF_INET, socket.SOCK_STREAM)
		clientSocket.connect((‘int(Host_IP)’, int(Host_Port))
		clientSocket.send(bytes(‘name', ‘UTF-8’))
		
		print("Codemeplease")
		
	def join_game(self):
		#TODO
		print("Codemeplease")
	#return 2 cards
	#call after get game state indicates server is ready.
	def bet(self,bet):
	#todo
	print("CodeMePlease.")
		
	#server responds with this game state
	#and whether it requires a decision from the client. 
	def get_game_state(self):
		
	#call after game state, indicates server is ready. 
	#Choice is to draw or pass, repeats until the end of the game.
	#should return the state of the game.
	#Server may reject and ask again.
	def play_round(self, choice):
	
		print("codemeplease")
	pass
		
class BlackJackServer():
	def set_players(self, no_of_players):
		
		
	def play_game(self, no_of_players):
		#accept bids.
		#play rounds. 
		#Declare winner. 
		#Verify priority. 
		#
		
		
		
class Deck:
	def __init__(self):
		self.cards = []
	
	def  addcard(self, card):
		self.cards.append(card)
	
	def draw(self):
		drawnCard = self.cards[0]
		self.cards.remove(self.cards[0])
		return drawnCard
	def shuffle(self):
		random.shuffle(self.cards)


class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit



deck = []

deck.append(Card(2, "Spades"))
deck.append(Card(3, "Spades"))
deck.append(Card(4, "Spades"))
deck.append(Card(5, "Spades"))
deck.append(Card(6, "Spades"))
deck.append(Card(7, "Spades"))
deck.append(Card(8, "Spades"))
deck.append(Card(9, "Spades"))
deck.append(Card(10, "Spades"))
deck.append(Card("Jack", "Spades"))
deck.append(Card("Queen", "Spades"))
deck.append(Card("King", "Spades"))
deck.append(Card("Ace", "Spades"))


#draw a random card
deck.shuffle()
card = deck.draw()
print("you got:" + str(card.value) + "of" + card.suit)
