import random
import sys
import socket
import logging
from miniboa import TelnetServer

IDLE_TIMEOUT = 500
CLIENT_LIST = []
SERVER_RUN = True
activeplayers = []
def on_connect(client):
    """
    Sample on_connect function.
    Handles new connections.
    """
    logging.info("Opened connection to {}".format(client.addrport()))
    broadcast("{} is being dealt in.\n".format(client.addrport()))
    CLIENT_LIST.append(client)
    client.send("Welcome to the Lions Head, {}.\n".format(client.addrport()))
	
def on_disconnect(client):
    """
    Sample on_disconnect function.
    Handles lost connections.
    """
    logging.info("Lost connection to {}".format(client.addrport()))
    CLIENT_LIST.remove(client)
    broadcast("{} Has left the table.\n".format(client.addrport()))
	
def kick_idle():
    """
    Looks for idle clients and disconnects them by setting active to False.
    """
    # Who hasn't been typing?
    for client in CLIENT_LIST:
        if client.idle() > IDLE_TIMEOUT:
            logging.info("Kicking idle lobby client from {}".format(client.addrport()))
            client.active = False
def process_clients():
    """
    Check each client, if client.cmd_ready == True then there is a line of
    input available via client.get_command().
    """
    for client in CLIENT_LIST:
        if client.active and client.cmd_ready:
            # If the client sends input echo it to the chat room
            chat(client)

def broadcast(msg):
    """
    Send msg to every client.
    """
    for client in CLIENT_LIST:
        client.send(msg)

def chat(client):
    """
    Echo whatever client types to everyone.
    """
    global SERVER_RUN
    msg = client.get_command()
    logging.info("{} says '{}'".format(client.addrport(), msg))

    for guest in CLIENT_LIST:
        if guest != client:
            guest.send("{} says '{}'\n".format(client.addrport(), msg))
        else:
            guest.send("You say '{}'\n".format(msg))

    cmd = msg.lower()
	# Begin Blackjack(AI)
    if cmd == 'run':
        PlayAI(client)
    # bye = disconnect
    elif cmd == 'bye':
        client.active = False
    # shutdown == stop the server
    elif cmd == 'shutdown':
        SERVER_RUN = False

def PlayAI(client):
	activeplayers.insert(0, 'client.addrport')
	activeplayers[0] = BlackjackGame
	game = activeplayers[0]
	game.run()
			
	def client_print(Message):
		while True:
			for client in CLIENT_LIST:
				client.send("{}".format(Message))
				return

	def get_input(question):
		while True:
			for client in CLIENT_LIST:
				value = client.get_command()
				client.send("{} ;response? '{}'\n".format(question, value))
			value = str(value)
			if value.startswith('y'):
				return 'y'
			elif value.startswith('n'):
				return 'n'
			elif value.startswith('q'):
				sys.exit(0)
			elif value.startswith('h'):
				client_print('one day you will have many options to choose from. For now you can quit at any time by typing q')
			else:
				client_print('Please choose yes, no, or quit.')

	def get_number(question):
		while True:
			for client in CLIENT_LIST:
				value = client.get_command()
				client.send("{} ;response? '{}'\n".format(question, value))
			if not value.isdigit():
				client_print('Please type a number')
			elif int(value) >self:
				client_print('Please, kid, you do not have that kind of cash')
			else:
				return int(value)

class BlackjackGame():
	# constants, should be the same for every class
	cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
	#suits = ('♠','♥','♦','♣')
	suits = ('S','H','D','C')
	
	def __init__(self):
		self.deck = []
		self.money = 500
		self.cpumoney = 500
		self.reset_game()
		Game_Over = False
	
	def reset_game(self):
		self.reset_deck()
		self.hand = []
		self.cpuhand = []
		self.cpufold = False
		self.cpubet = 0
		self.cpuraise = 0
		self.cpumatch = 0
		self.playerbet = 0
		self.playerraise = 0
		self.playerbet2 = 0
		self.playertotalbet = 0
		self.pot = 0
		self.aggrobet = False
	
	def reset_deck(self):
		self.deck.clear()
		for s in self.suits:
			for c in self.cards:
				self.deck.append((s, c))
		random.shuffle(self.deck)
		
	def check_hand(self, hand_list):
		score = 0
		aces = 0
		for c in hand_list:
			if c[1] == 'A':
				score += 1
				aces += 1
			elif c[1] in ('J', 'Q', 'K'):
				score += 10
			else:
				score += int(c[1])
		
		for i in range(aces):
			if score + 10 <= 21:
				score += 10
			else:
				break
		
		return score

	def draw_cards(self, number=1):
		result = []
		for i in range(number):
			result.append(self.deck.pop())
		return result
		
	def run():
		globalclient_print("""Outside the window of the Lion's Head Tavern, the west wind is urging the ocean \n into an assault on the docks and rattling windows all along the quayside. 
		The bartender has stopped relocating grime from one glass to another and is instead keeping \n	 a careful eye on the ceiling, occasionally moving mugs and glasses \n		to catch the droplets of water leaking from the rafters.
		The smell of wet wood and salt has overpowered the lingering aroma of alcohol and \n the man across from you inhales deeply as he shuffles the tattered deck.""")
		hasplayed = get_input("""\"Well now\", his rough voice cuts through the soft sigh of water against the cobbles,\"is this your first time playing blackjack?\": """)
		if hasplayed == "y":
			showrules = get_input("Do you want me to explain the rules?: ")
			if showrules == "y":
				client_print("""Blackjack is simple, just try to get as close to 21 without going over. Face cards are ten, aces are one or eleven, your choice. Maybe once you improve we'll introduce splittin' and doubling down.""")
			else:
				client_print("Entirely up to you. I don't mind taking your money.")
		if hasplayed == "n": 
			client_print("Well, we'd best get started then, kid.")
		self.__init__()
		while True: 
			self.reset_game()
			hand += self.draw_cards(2)
			cpuhand += self.draw_cards(2)
			client_print("Hand: {} (score {})".format(hand, self.check_hand(hand)) )
			if self.check_hand(cpuhand) == 21:
				client_print("I'll wager a little.")
				cpubet = random.randint(5,50)
				pot += cpubet
				client_print(cpubet)
			elif self.check_hand(cpuhand) < 10:
				client_print("I'll see this hand through.")
				cpubet = random.randint(1,20)
				pot += cpubet
				client_print(cpubet)
			else:
				client_print("I'll bet:")
				cpubet = random.randint(3,30)
				pot += cpubet
				client_print(cpubet)
			playerbet = get_number("How much do you wanna lose?: ")
			pot += playerbet
			playertotalbet = playerbet
			hit = get_input("Wanna draw another?: ")
			if hit == "n":
				cpubust = False
				if self.check_hand(cpuhand) < 16 :
					client_print("I'm taking another card")
					cpuhand += self.draw_cards()
					if self.check_hand(cpuhand) > 21:
						client_print("Balls, I'm bust.")
						cpubust = True
					elif self.check_hand(cpuhand) >= 16:
						client_print("I'll stay. I'm just fine.")
					elif self.check_hand(cpuhand) < 16 :
						client_print("I'll hit again")
						cpuhand += self.draw_cards()
						if self.check_hand(cpuhand) > 21:
							client_print("Balls, I'm bust.")
							cpubust = True
						elif self.check_hand(cpuhand) <= 21 :
							client_print("I'll stay. I'm just fine.")
						elif self.check_hand(cpuhand) < 16 :
							client_print("I like my luck. I'll take one more.")
							cpuhand += self.draw_cards()
							if self.check_hand(cpuhand) > 21:
								client_print("Balls, I'm bust.")
								cpubust = True
							elif self.check_hand(cpuhand) <= 21: 
								client_print ("Well, well. Get ready kid.")
								aggrobet = True 
				if cpubust == False:
					checkorraise = get_input("Think you have a good hand. Well, prepared to match my bet?: ")
					if checkorraise == "y":
						cpuraise = random.randint(0,100)
						if aggrobet == True:
							cpuraise = cpuraise + 100
						pot = int(pot) + int(cpuraise)
						client_print("I've put in" )
						client_print(cpuraise)
						client_print("you're gonna have to match it or raise.")
						playerraise = get_number("pick a number: ")
						if int(playerraise) < int(cpuraise):
							client_print("That ain't enough kid, weren't you listening?")
							client_print("I've put in" )
							client_print(cpuraise)
							client_print("you're gonna have to match it or raise.")
							playerraise = get_input("I'm going to put in: ")
						playertotalbet = int(playertotalbet) + int(playerraise)
						pot = int(pot) + int(cpuraise) + int(playerraise)
						if int(playerraise) > int(cpuraise):
							if sum(pot) < 200 and int(cpuhand) > 21:
								client_print("that's a lotta money kid you sure you wanna lose more?")
								cpumatch = playerraise
								pot += int(cpumatch)
							if sum(pot) < 200 and int(cpuhand) < 21:
								client_print("Too rich for me")
								cpufold = True
						
			if hit == "y":
				hand += self.draw_cards()
				client_print("Hand: {} (score {})".format(hand, self.check_hand(hand)) )
				hit = get_input("Careful you don't bust there kid. Sure you wanna draw another?: ")
				if hit == "y":
					hand += self.draw_cards()
					client_print("Hand: {} (score {})".format(hand, self.check_hand(hand)) )
					hit = get_input("Going all the way to five cards?: ")
				if hit == "y":
					hand += self.draw_cards()
					client_print("Hand: {} (score {})".format(hand, self.check_hand(hand)) )
				if hit in ["n", "y"]:
					if self.check_hand(cpuhand) > 19 :
						client_print("I think I'll stay")
					if self.check_hand(cpuhand) < 16 :
						client_print("Just one more for me")
						cpuhand += self.draw_cards()
					if self.check_hand(cpuhand) > 21 :
						client_print("I'll stay. I'm just fine.")
					if self.check_hand(cpuhand) < 16 :
						client_print("I'll test my luck")
						cpuhand += self.draw_cards()
						if self.check_hand(cpuhand) > 20 :
							client_print("I'll stay. I'm just fine.")
						if self.check_hand(cpuhand) < 16 :
							client_print("I like my luck. I'll take one more.")
							cpuhand += self.draw_cards()
							if self.check_hand(cpuhand) >= 21: 
								client_print ("Well, well. Get ready kid.")
								aggrobet == True 
				checkorraise = get_input("Think you have a good hand. Well, ready to put money on it?: ")
				if checkorraise == "y":
					cpuraise = random.randint(0,50)
					if aggrobet == True:
						cpuraise = cpuraise + 100
					pot += int(cpuraise)
					client_print(cpuraise)
					client_print("That's my bet.")
					playerbet2 = get_number("I think I'll bet: ")
					playertotalbet = int(playertotalbet) + int(playerbet2)
					pot += int(playerbet2)
					if int(playerbet2) > int(cpuraise):
						client_print("Bold move Kid.")
						if self.check_hand(cpuhand) < 19:
							client_print("I fold")
							cpufold = True
						else:
							client_print("I'll bite.")
							cpuraise = playerbet2
							pot += int(cpuraise)
							
			client_print("Time to show our cards")
			client_print("You've got")
			client_print("Hand: {} (score {})".format(hand, self.check_hand(hand)) )
			client_print("Here's my cards")
			client_print("Hand: {} (score {})".format(cpuhand, self.check_hand(cpuhand)) )
			
			if self.check_hand(hand) == 21 and len(hand) == 2:
				client_print("That's Blackjack. Nice one kid")
				
			if self.check_hand(hand) < self.check_hand(cpuhand):
				if cpufold == True:
					client_print("Damn, should've held out.")
					client_print(pot)
					money -= int(playertotalbet)
					money += int(pot)
					cpumoney -= int(cpumatch)
					cpumoney -= int(cpuraise)
					cpumoney -= int(cpubet)
				elif self.check_hand(cpuhand) > 21:
					client_print("I went bust. Take the pot.")
					client_print(pot)
					money -= int(playertotalbet)
					money += int(pot)
					cpumoney -= int(cpumatch)
					cpumoney -= int(cpuraise)
					cpumoney -= int(cpubet)
				else:	
					client_print("Not quite kid")
					client_print("you lost")
					client_print(playertotalbet)
					money = int(money) - int(playertotalbet)
					cpumoney -= int(cpumatch)
					cpumoney -= int(cpuraise)
					cpumoney -= int(cpubet)
					cpumoney += int(pot)
			elif self.check_hand(hand) > self.check_hand(cpuhand):
				if cpufold == True:
					client_print("Just glad I didn't lose more.")
					client_print(pot)
					money -= int(playertotalbet)
					money += int(pot)
					cpumoney -= int(cpumatch)
					cpumoney -= int(cpuraise)
					cpumoney -= int(cpubet)
				elif self.check_hand(hand) > 21:
					client_print("You're bust kid. better luck next time.")
					client_print("you lost")
					client_print(playertotalbet)
					money = int(money) - int(playertotalbet)
					cpumoney -= int(cpumatch)
					cpumoney -= int(cpuraise)
					cpumoney -= int(cpubet)
					cpumoney += int(pot)
				else:
					client_print("You win kid. Good Job.")
					client_print("Your winnings, ")
					client_print(pot)
					money += int(pot)
					money -= int(playertotalbet)
					cpumoney -= int(cpuraise)
					cpumoney -= int(cpubet)
			elif self.check_hand(hand) == self.check_hand(cpuhand):
				client_print("That's what's known as a \"push\", son.")
				
			client_print("I've got this much money left:")
			client_print(money)
			client_print("He has this much money left: ")
			client_print(cpumoney)
			if money < 0:
				client_print("You've lost it all Kid, just give up already.")
				Game_Over = True
			if cpumoney < 0:
				client_print("Well, I guess that wasn't luck I was feeling. You've bled me dry, nice work, kid.")
			
			
if __name__ == "__main__":
     logging.basicConfig(level=logging.DEBUG)
	 
     telnet_server = TelnetServer(
        port=8089,
        address='',
        on_connect=on_connect,
        on_disconnect=on_disconnect,
        timeout = .05
        )    
     logging.info("Listening for connections on port {}. CTRL-C to break.".format(telnet_server.port))
     while SERVER_RUN:
        telnet_server.poll()        # Send, Recv, and look for new connections
        kick_idle()                 # Check for idle clients
        process_clients()           # Check for client input

     logging.info("Server shutdown.")
       


	
	
