import random
import sys

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
		value = input(question).lower()
		if value.startswith('y'):
			return 'y'
		elif value.startswith('n'):
		    return 'n'
		elif value.startswith('q'):
		    sys.exit(0)
		elif value.startswith('h'):
			print('one day you will have many options to choose from. For now you can quit at any time by typing q')
		else:
			print('Please choose yes, no, or quit.')

def get_number(question):
	while True:
		value = input(question)
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
		
	print("""Outside the window of the Lion's Head Tavern, the west wind is urging the ocean \n into an assault on the docks and rattling windows all along the quayside. 
	The bartender has stopped relocating grime from one glass to another and is instead keeping \n	 a careful eye on the ceiling, occasionally moving mugs and glasses \n		to catch the droplets of water leaking from the rafters.
	The smell of wet wood and salt has overpowered the lingering aroma of alcohol and \n the man across from you inhales deeply as he shuffles the tattered deck.""")
	hasplayed = get_input("\"Well now\", his rough voice cuts through the soft sigh of water against the cobbles,\"is this your first time playing blackjack?\": ")
	if hasplayed == "y":
		showrules = get_input("Do you want me to explain the rules?: ")
		if showrules == "y":
			print("Blackjack is simple, just try to get as close to 21 without going over. Face cards are ten, aces are one or eleven, your choice. Maybe once you improve we'll introduce splittin' and doubling down.")
		else:
			print("Entirely up to you. I don't mind taking your money.")
	if hasplayed == "n": 
		print("Well, we'd best get started then, kid.")
				
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
		print("Hand: {} (score {})".format(hand, check_hand(hand)) )
		if check_hand(cpuhand) == 21:
			print("I'll wager a little.")
			cpubet = random.randint(5,50)
			pot += cpubet
			print(cpubet)
		elif check_hand(cpuhand) < 10:
			print("I'll see this hand through.")
			cpubet = random.randint(1,20)
			pot += cpubet
			print(cpubet)
		else:
			print("I'll bet:")
			cpubet = random.randint(3,30)
			pot += cpubet
			print(cpubet)
		playerbet = get_number("How much do you wanna lose?: ")
		pot += playerbet
		playertotalbet = playerbet
		hit = get_input("Wanna draw another?: ")
		if hit == "n":
			cpubust = False
			if check_hand(cpuhand) < 16 :
				print("I'm taking another card")
				cpuhand += draw_cards(deck)
				if check_hand(cpuhand) > 21:
					print("Balls, I'm bust.")
					cpubust = True
				elif check_hand(cpuhand) >= 16:
					print("I'll stay. I'm just fine.")
				elif check_hand(cpuhand) < 16 :
					print("I'll hit again")
					cpuhand += draw_cards(deck)
					if check_hand(cpuhand) > 21:
						print("Balls, I'm bust.")
						cpubust = True
					elif check_hand(cpuhand) <= 21 :
						print("I'll stay. I'm just fine.")
					elif check_hand(cpuhand) < 16 :
						print("I like my luck. I'll take one more.")
						cpuhand += draw_cards(deck)
						if check_hand(cpuhand) > 21:
							print("Balls, I'm bust.")
							cpubust = True
						elif check_hand(cpuhand) <= 21: 
							print ("Well, well. Get ready kid.")
							aggrobet = True 
			if cpubust == False:
				checkorraise = get_input("Think you have a good hand. Well, prepared to match my bet?: ")
				if checkorraise == "y":
					cpuraise = random.randint(0,100)
					if aggrobet == True:
						cpuraise = cpuraise + 100
					pot = int(pot) + int(cpuraise)
					print("I've put in" )
					print(cpuraise)
					print("you're gonna have to match it or raise.")
					playerraise = get_number("pick a number: ")
					if int(playerraise) < int(cpuraise):
						print("That ain't enough kid, weren't you listening?")
						print("I've put in" )
						print(cpuraise)
						print("you're gonna have to match it or raise.")
						playerraise = input("I'm going to put in: ")
					playertotalbet = int(playertotalbet) + int(playerraise)
					pot = int(pot) + int(cpuraise) + int(playerraise)
					if int(playerraise) > int(cpuraise):
						if int(pot) < 200 and int(cpuhand) > 21:
							print("that's a lotta money kid you sure you wanna lose more?")
							cpumatch = playerraise
							pot += int(cpumatch)
						if int(pot) < 200 and int(cpuhand) < 21:
							print("Too rich for me")
							cpufold = True
					
		if hit == "y":
			hand += draw_cards(deck)
			print(hand)
			hit = get_input("Careful you don't bust there kid. Sure you wanna draw another?: ")
			if hit == "y":
				hand += draw_cards(deck)
				print(hand)
				hit = get_input("Going all the way to five cards?: ")
			if hit == "y":
				hand += draw_cards(deck)
				print(hand)
			if hit in ["n", "y"]:
				if check_hand(cpuhand) > 19 :
					print("I think I'll stay")
				if check_hand(cpuhand) < 16 :
					print("Just one more for me")
					cpuhand += draw_cards(deck)
				if check_hand(cpuhand) > 21 :
					print("I'll stay. I'm just fine.")
				if check_hand(cpuhand) < 16 :
					print("I'll test my luck")
					cpuhand += draw_cards(deck)
					if check_hand(cpuhand) > 20 :
						print("I'll stay. I'm just fine.")
					if check_hand(cpuhand) < 16 :
						print("I like my luck. I'll take one more.")
						cpuhand += draw_cards(deck)
						if check_hand(cpuhand) >= 21: 
							print ("Well, well. Get ready kid.")
							aggrobet == True 
			checkorraise = get_input("Think you have a good hand. Well, ready to put money on it?: ")
			if checkorraise == "y":
				cpuraise = random.randint(0,50)
				if aggrobet == True:
					cpuraise = cpuraise + 100
				pot += int(cpuraise)
				print(cpuraise)
				print("That's my bet.")
				playerbet2 = get_number("I think I'll bet: ")
				playertotalbet = int(playertotalbet) + int(playerbet2)
				pot += int(playerbet2)
				if int(playerbet2) > int(cpuraise):
					print("Bold move Kid.")
					if check_hand(cpuhand) < 19:
						print("I fold")
						cpufold = True
					else:
						print("I'll bite.")
						cpuraise = playerbet2
						pot += int(cpuraise)
						
		print("Time to show our cards")
		print("You've got")
		print("Hand: {} (score {})".format(hand, check_hand(hand)) )
		print("Here's my cards")
		print("Hand: {} (score {})".format(cpuhand, check_hand(cpuhand)) )
		
		if check_hand(hand) == 21 and len(hand) == 2:
			print("That's Blackjack. Nice one kid")
			
		if check_hand(hand) < check_hand(cpuhand):
			if cpufold == True:
				print("Damn, should've held out.")
				print(pot)
				money -= int(playertotalbet)
				money += int(pot)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
			elif check_hand(cpuhand) > 21:
				print("I went bust. Take the pot.")
				print(pot)
				money -= int(playertotalbet)
				money += int(pot)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
			else:	
				print("Not quite kid")
				print("you lost")
				print(playertotalbet)
				money = int(money) - int(playertotalbet)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
				cpumoney += int(pot)
		elif check_hand(hand) > check_hand(cpuhand):
			if cpufold == True:
				print("Just glad I didn't lose more.")
				print(pot)
				money -= int(playertotalbet)
				money += int(pot)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
			elif check_hand(hand) > 21:
				print("You're bust kid. better luck next time.")
				print("you lost")
				print(playertotalbet)
				money = int(money) - int(playertotalbet)
				cpumoney -= int(cpumatch)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
				cpumoney += int(pot)
			else:
				print("You win kid. Good Job.")
				print("Your winnings, ")
				print(pot)
				money += int(pot)
				money -= int(playertotalbet)
				cpumoney -= int(cpuraise)
				cpumoney -= int(cpubet)
		elif check_hand(hand) == check_hand(cpuhand):
			print("That's what's known as a \"push\", son.")
			
		print("I've got this much money left:")
		print(money)
		print("He has this much money left: ")
		print(cpumoney)
		if money < 0:
			print("You've lost it all Kid, just give up already.")
		if cpumoney < 0:
			print("Well, I guess that wasn't luck I was feeling. You've bled me dry, nice work, kid.")
			
			
if __name__ == "__main__":
	run()
