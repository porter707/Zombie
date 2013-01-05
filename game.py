import random, sys

class character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def quit(self, encounter):
        print ("%s searches for an escape, but gets cornered by a horde of Zombies, your body was ripped apart and eaten..." % self.name)
        print ("%s survived for a few more days before being eaten during his sleep..." %hero_2.name)
        print ("It is unknown what happened to %s."%hero_3.name)
        sys.exit()

    def help(self, encounter):
        print Commands.keys()

    def explore(self, encounter):
        if encounter == True:
            print ("You can't explore right now...")
            encounter = True
        else:
            route = random.randint(0, 9)
            if route == 1:
                print ("You walk down a dark lane, looking for supplies.")
            elif route == 2:
                print ("You see a building with a light on inside, you go to explore.")
            elif route == 3:
                print ("You find a carpark, and decide to check the area.")
            elif route == 4:
                print ("You slip past a horde of zombies and search the militry camp.")
            elif route == 5:
                print ("You hear a sound coming from a nearby building and decide to explore.")
            elif route == 6:
                print ("You think you see a person running, and decide to follow.")
            elif route == 7:
                print ("You walk the streets in hope of finding something.")
            elif route == 8:
                print ("You enter the construction site looking for useful supplies.")
            else:
                print ("You explored the area but found nothing of interest.")
            encounter = False
        return encounter

    def flee(self, encounter):
        if encounter == True:
            runchance = random.randint(0, 2)
            if runchance == 1:
                print ("You successfully got away.")
                encounter = False
            else:
                print ("You tried to run but got trapped by zombies.")
                encounter = True
                deathchance = random.randint(0,11)
                if deathchance == 1:
                    print ("You look for an escape, but you're surrounded...")
                    raw_input("...")
                    print ("You close your eyes and accpet your fate...")
                    sys.exit()
        else:
            print("There is no need to flee right now.")
            encounter = False
        return encounter
            
    def attack(self, encounter):
        if encounter == True:
            hitchance = random.randint(0, 2)
            if hitchance == 1:
                print ("You struck the zombie with a crowbar, it falls to the ground.")
                encounter = False
            else:
                deathchance = random.randint(0, 2)
                if deathchance == 1:
                    print ("You struck the zombie with a crowbar, it falls to the ground and grabs hold of your leg, taking a bite...")
                    raw_input("...")
                    print ("As you try to run the horde catches up with you and pin you to the ground, slowly eating you alive...")
                    print ("It is unknown what happened to the your friends that day...")
                    sys.exit()
                else:
                    print ("You tried to strike the zombie but missed...")
                    encounter = True
        else:
            print ("There is no need to attack anything right now.")
        return encounter
                    
            
  
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
    if zombie <= 5:
        encounter = True
        print ("Zombies walk towards you")
        while encounter == True:
            encounter_option = raw_input('>')
            if encounter_option in Commands.keys():
                encounter = Commands [encounter_option] (hero, encounter)
            else:
                print ("The Zombies get closer...")
    else:
        encounter = False

    if choice in Commands.keys():
        Commands [choice] (hero, encounter)
    else:
        print ("I didn't understand that command...")
