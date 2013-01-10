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
            subroute = random.randint(0,4)
            if route == 1:
                print ("You walk down a dark lane, looking for supplies.")
                if subroute == 1:
                    print ("You found some food and drink, scattered around the lane.")
                elif subroute == 2:
                    print("You found nothing in the lane, but avoided a horde of passing zombies")
                elif subroute == 3:
                    print ("A horde of zombies block your exit from the lane, you and your friends try to fight off the horde...")
                    raw_input("...")
                    print ("%s scraficed his life, in an attempt to save you...\nYou tried to push through the horde taking down a few zombies.\nA zombie grabs hold of your back and bites you...\nyou manage to escape but eventually give up and sit down and wait for it to end. "% hero_2.name)
                    sys.exit()
                else:
                    print ("You found nothing of interest.")
                
            elif route == 2:
                print ("You see a building with a light on inside, you go to explore.")
                if subroute == 1:
                    print ("You find some tins of food on the floor, it looks like someone has recently been staying here.")
                elif subroute == 2:
                    print("As you enter the house, you see eaten remains of some people.")
                elif subroute == 3:
                    print ("You enter the house and find nothing, but avoid a horde of zombies.")
                else:
                    print ("You found nothing of interest.")
            elif route == 3:
                print ("You find a carpark, and decide to check the area.")
                if subroute == 1:
                    print ("You try the doors on some cars but they are all locked.")
                elif subroute == 2:
                    print("You see a car with an open door, you enter the car but the keys are missing.")
                elif subroute == 3:
                    print ("You see a car with the engine running, you go towards the car but notice a horde of zombies around it.")
                    raw_input("...")
                    print ("You try to fight of the horde, you see your chance and jump in the car...\nAs you put the car into gear a zombie grabs hold of you, %s pulls the zombie away from you and kills it as he turns around another zombie manages to bite him.\nYou get out of the car and kill the zombie, eventually you all get in the car and drive away.\nIt is unkown if anyone survived."% hero_3.name)
                    sys.exit()
                else:
                    print ("You found nothing of interest.")
            elif route == 4:
                print ("You slip past a horde of zombies and search the militry camp.")
                if subroute == 1:
                    print ("You find some useful survival gear.")
                elif subroute == 2:
                    print("As you look around the camp you notice that it is overrun and decide to leave.")
                elif subroute == 3:
                    print ("You enter the camp and find some rifles, a horde of zombies approch and you fire at them, they fall to the ground.")
                    raw_input("...")
                    print ("The noise made from firing the guns alert all the nearby hordes of zombies, you try to hold out as long as you can, but eventually get overrun.")
                    sys.exit()
                else:
                    print ("You found nothing of interest.")
            elif route == 5:
                print ("You hear a sound coming from a nearby building and decide to explore.")
                if subroute == 1:
                    print ("You enter a the building and find a man being eaten alive, you kill the zombie and leave.")
                elif subroute == 2:
                    print("You enter the building to find a radio making a noise, you try to use the radio to call for help but get no response.")
                elif subroute == 3:
                    print ("You find nothing in the building and couldn't work out where the sound was coming from.")
                else:
                    print ("You found nothing of interest.")
            elif route == 6:
                print ("You think you see a person running, and decide to follow.")
                if subroute == 1:
                    print ("You try to catch up with the person, but lost them.")
                elif subroute == 2:
                    print("You try to catch up with the person but run into a horde of zombies and are forced to run back.")
                elif subroute == 3:
                    print ("You catch up with the person and get them to stop.")
                    raw_input("...")
                    print ("You talk to the person who turns out to be a young girl, she explains to you that ")
                    sys.exit()
                else:
                    print ("You found nothing of interest.")
            elif route == 7:
                print ("You walk the streets in hope of finding something.")
                if subroute == 1:
                    print ("")
                elif subroute == 2:
                    print("")
                elif subroute == 3:
                    print ("")
                    raw_input("...")
                    print ("")
                    sys.exit()
                else:
                    print ("You found nothing of interest.")
            elif route == 8:
                print ("You enter the construction site looking for useful supplies.")
                if subroute == 1:
                    print ("")
                elif subroute == 2:
                    print("")
                elif subroute == 3:
                    print ("")
                    raw_input("...")
                    print ("")
                    sys.exit()
                else:
                    print ("You found nothing of interest.")
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
