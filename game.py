import pygame, random, sys

class character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def quit(self):
        print ("%s searches for an escape, but gets cornered by a horde of Zombies, your body was ripped apart and eaten..." % self.name)
        print ("%s survived for a few more days before being eaten during his sleep..." %hero_2.name)
        print ("It is unknown what happened to %s."%hero_3.name)
        sys.exit()

    def help(self):
        print Commands.keys()

    def explore(self):
        route = random.randint(0, 10)

    def flee(self):
    	if encounter == True:
		runchance = random.randint(0, 2)
		if runchance == 1:
			print ("You successfully got away.")
			encounter = False
            	else:
			print ("You tried to run but got trapped by zombies.")
	else:
            print("There is no need to flee right now.")
            
    def attack(self):
        hitchance = random.randint(0, 2)
  
Commands = {
  'quit': character.quit,
  'help': character.help,
  'explore': character.explore,
  'flee': character.flee,
  'attack': character.attack,
  }

print ("It's been 12 weeks since the start of the outbreak...")
raw_input('...')
print ("You and two other survivors made it to an army camp.")
raw_input('...')
print ("The one survivor is a young male named..")
friend_1 = raw_input('>')
print ("The other is a older male named..")
friend_2 = raw_input('>')
print ("Your name is..")
player = raw_input('>')

hero = character(player, 100, 20)
hero_2 = character(friend_1, 100, 20)
hero_3 = character(friend_2, 100, 20)

print ("You quickly realised that the camp was overrun and was not safe..")
raw_input('...')

while True:
	choice = raw_input('>')
	zombie = random.randint(0,11)
	if zombie == 5:
		encounter = True
		print ("A lone Zombie walks towards you")
	elif zombie == 7:
		print ("A horde of Zombies run towards you")
       		encounter = True
	else:
		encounter = False

	if choice in Commands.keys():
		Commands [choice] (hero)
	else:
		print ("I didn't understand that command...")
