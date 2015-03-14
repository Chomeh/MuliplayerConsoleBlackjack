import random
import sys
import socket

#Connect to client.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8089))
BUFFER_SIZE = 1024

def client_print(Message):
	s.listen(1)
	while True:
		print(Message)
		c = s.accept()
		cli_sock, cli_addr = c 
		cli_sock.send(bytes(Message, 'UTF-8'))
		return
    
	
	
    

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#suits = ['♠','♥','♦','♣']
suits = ['S','H','D','C']
deck = []

def reset_deck():
	deck = []
	for s in suits:
		for c in cards:
			deck.append((s, c))
	random.shuffle(deck)
	return deck
	
def check_hand(hand_list):
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

def draw_cards(deck_list, number=1):
	result = []
	for i in range(number):
		result.append(deck_list.pop())
	return result
	
def get_input(question):
	while True:
		c = s.accept()
		cli_sock, cli_addr = c
		qquestion = ("q"+ question)
		cli_sock.send(bytes(qquestion, 'UTF-8'))
		data = cli_sock.recv(BUFFER_SIZE)
		value = data
		if value.startswith(b'y'):
			return 'y'
		elif value.startswith(b'n'):
		    return 'n'
		elif value.startswith(b'q'):
		    sys.exit(0)
		elif value.startswith(b'h'):
			print('one day you will have many options to choose from. For now you can quit at any time by typing q')
		else:
			print('Please choose yes, no, or quit.')

def get_number(question):
	while True:
		c = s.accept()
		cli_sock, cli_addr = c
		nquestion = ("n"+ question)
		cli_sock.send(bytes(nquestion, 'UTF-8'))
		data = cli_sock.recv(BUFFER_SIZE)
		value = data
		if not value.isdigit():
			print('Please type a number')
		elif int(value) >1000:
			print('Please, kid, you do not have that kind of cash')
		else:
			return int(value)

			
def run():
	money = 500
	cpumoney = 500
	aggrobet = False
		
	client_print("""Outside the window of the Lion's Head Tavern, the west wind is urging the ocean \n into an assault on the docks and rattling windows all along the quayside. 
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
		
	while True:
		
		deck = reset_deck()
		hand = []
		cpuhand = []
		cpufold = False
		cpubet = 0
		cpuraise = 0
		cpumatch = 0
		playerbet = 0
		playerraise = 0
		playerbet2 = 0
		playertotalbet = 0
		pot = 0 
		hand += draw_cards(deck, 2)
		cpuhand += draw_cards(deck, 2)
		client_print("Hand: {} (score {})".format(hand, check_hand(hand)) )
		if check_hand(cpuhand) == 21:
			client_print("I'll wager a little.")
			cpubet = random.randint(5,50)
			pot += cpubet
			client_print(cpubet)
		elif check_hand(cpuhand) < 10:
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
			if check_hand(cpuhand) < 16 :
				client_print("I'm taking another card")
				cpuhand += draw_cards(deck)
				if check_hand(cpuhand) > 21:
					client_print("Balls, I'm bust.")
					cpubust = True
				elif check_hand(cpuhand) >= 16:
					client_print("I'll stay. I'm just fine.")
				elif check_hand(cpuhand) < 16 :
					client_print("I'll hit again")
					cpuhand += draw_cards(deck)
					if check_hand(cpuhand) > 21:
						client_print("Balls, I'm bust.")
						cpubust = True
					elif check_hand(cpuhand) <= 21 :
						client_print("I'll stay. I'm just fine.")
					elif check_hand(cpuhand) < 16 :
						client_print("I like my luck. I'll take one more.")
						cpuhand += draw_cards(deck)
						if check_hand(cpuhand) > 21:
							client_print("Balls, I'm bust.")
							cpubust = True
						elif check_hand(cpuhand) <= 21: 
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
						if int(pot) < 200 and int(cpuhand) > 21:
							client_print("that's a lotta money kid you sure you wanna lose more?")
							cpumatch = playerraise
							pot += int(cpumatch)
						if int(pot) < 200 and int(cpuhand) < 21:
							client_print("Too rich for me")
							cpufold = True
					
		if hit == "y":
			hand += draw_cards(deck)
			client_print("Hand: {} (score {})".format(hand, check_hand(hand)) )
			hit = get_input("Careful you don't bust there kid. Sure you wanna draw another?: ")
			if hit == "y":
				hand += draw_cards(deck)
				client_print("Hand: {} (score {})".format(hand, check_hand(hand)) )
				hit = get_input("Going all the way to five cards?: ")
			if hit == "y":
				hand += draw_cards(deck)
				client_print("Hand: {} (score {})".format(hand, check_hand(hand)) )
			if hit in ["n", "y"]:
				if check_hand(cpuhand) > 19 :
					client_print("I think I'll stay")
				if check_hand(cpuhand) < 16 :
					client_print("Just one more for me")
					cpuhand += draw_cards(deck)
				if check_hand(cpuhand) > 21 :
					client_print("I'll stay. I'm just fine.")
				if check_hand(cpuhand) < 16 :
					client_print("I'll test my luck")
					cpuhand += draw_cards(deck)
					if check_hand(cpuhand) > 20 :
						client_print("I'll stay. I'm just fine.")
					if check_hand(cpuhand) < 16 :
						client_print("I like my luck. I'll take one more.")
						cpuhand += draw_cards(deck)
						if check_hand(cpuhand) >= 21: 
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
					if check_hand(cpuhand) < 19:
						client_print("I fold")
						cpufold = True
					else:
						client_print("I'll bite.")
						cpuraise = playerbet2
						pot += int(cpuraise)
						
		client_print("Time to show our cards")
		client_print("You've got")
		client_print("Hand: {} (score {})".format(hand, check_hand(hand)) )
		client_print("Here's my cards")
		client_print("Hand: {} (score {})".format(cpuhand, check_hand(cpuhand)) )
		
		if check_hand(hand) == 21 and len(hand) == 2:
			client_print("That's Blackjack. Nice one kid")
			
		if check_hand(hand) < check_hand(cpuhand):
			if cpufold == True:
				client_print("Damn, should've held out.")
				client_print(pot)
				money -= int(playertotalbet)
				money += int(pot)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
			elif check_hand(cpuhand) > 21:
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
		elif check_hand(hand) > check_hand(cpuhand):
			if cpufold == True:
				client_print("Just glad I didn't lose more.")
				client_print(pot)
				money -= int(playertotalbet)
				money += int(pot)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
			elif check_hand(hand) > 21:
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
		elif check_hand(hand) == check_hand(cpuhand):
			client_print("That's what's known as a \"push\", son.")
			
		client_print("I've got this much money left:")
		client_print(money)
		client_print("He has this much money left: ")
		client_print(cpumoney)
		if money < 0:
			client_print("You've lost it all Kid, just give up already.")
		if cpumoney < 0:
			client_print("Well, I guess that wasn't luck I was feeling. You've bled me dry, nice work, kid.")
			
			
if __name__ == "__main__":
	run()
