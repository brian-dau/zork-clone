# A Zork-like using OOP (I hope)

import sys, random

class Player:
    """The user interacting with the dungeon"""
    inventory = ['map']
    username = ""
    def __init__(self, name):
        """Initializes with the player's name"""
        Player.username = name
        print("Welcome to the dungeon, {}!".format(Player.username))
        print()
        print('To move, type "move" with a cardinal direction.')
        print('To check your location, type "map".')
        print('To check your inventory, type "inventory".')
        print('To examine something, type "examine" with a noun.')
        print('To get something, type "get" with a noun.')
        print('To use an item, type "use" with a noun or something from your inventory.')
        print('To quit, type "quit".')
        print('Type "help" to see this list again.')
        print()

    def check_inventory():
        print("Current inventory is: ", Player.inventory)

    def check_map():
        print("Current location is: ", Dungeon.location)

    def show_help():
        print()
        print('To move, type "move" with a cardinal direction.')
        print('To check your location, type "map".')
        print('To check your inventory, type "inventory".')
        print('To examine something, type "examine" with a noun.')
        print('To get something, type "get" with a noun.')
        print('To use an item, type "use" with a noun or something from your inventory.')
        print('To quit, type "quit".')
        print('Type "help" to see this list again.')
        print()

    def quit_game():
        print("Thanks for playing!")
        sys.exit()

class Dungeon:
    """The grid which the player can move through"""
    location = []
    xcoord = ""
    ycoord = ""
    doors = ""
    roomkey = {}
    width = 0
    height = 0
    text = ""
    def __init__(self, width, height, roominfo):
        """Initializes a list of tuples representing coordinates in a grid
        size width * height and starts the player in the center of the grid."""
        Dungeon.width = width
        Dungeon.height = height
        self.coordinates = [(self.x, self.y) for self.x in range(Dungeon.width) for self.y in range(Dungeon.height)]
        # Width, height should be odd and same value and match roominfo.txt
        Dungeon.location = list(self.coordinates[int((Dungeon.width * Dungeon.height - 1) / 2)])
        # Reads from text file roominfo and inputs it into a dictionary
        # where key is location tuple and value is room description as string
        with open(roominfo, "rt") as self.f:
            self.roomtext = self.f.read()
        self.roomlist = self.roomtext.split("\n")
        self.i = iter(self.roomlist)
        Dungeon.roomkey = dict(zip(self.i, self.i))

    def enter_room(self, room):
        """Takes the player's Dungeon.location and prints a description of the room"""
        Dungeon.xcoord, Dungeon.ycoord = str(room[0]), str(room[1])
        Dungeon.text = Dungeon.roomkey[Dungeon.xcoord+Dungeon.ycoord]
        print(Dungeon.text)
        Action.get_item = ""
        Action.use_item = ""
        if "lantern" in Dungeon.text:
            if Dungeon.doors != "solved":
                print("You hear the doors locking shut!")
                Dungeon.doors = "locked"

    def move(self, direction):
        """Takes a direction argument to move the player around the dungeon"""
        self.direction = direction
        if self.direction == "move north":
            if Dungeon.location[0] > 0:
                Dungeon.location[0] = Dungeon.location[0] - 1
                Dungeon.enter_room(self, Dungeon.location)
            else:
                print("Can't go any farther north.")
        elif self.direction == "move south":
            if Dungeon.location[0] < Dungeon.height - 1:
                Dungeon.location[0] = Dungeon.location[0] + 1
                Dungeon.enter_room(self, Dungeon.location)
            else:
                print("Can't go any farther south.")
        elif self.direction == "move east":
            if Dungeon.location[1] < Dungeon.width - 1:
                Dungeon.location[1] = Dungeon.location[1] + 1
                Dungeon.enter_room(self, Dungeon.location)
            else:
                print("Can't go any farther east.")
        elif self.direction == "move west":
            if Dungeon.location[1] > 0:
                Dungeon.location[1] = Dungeon.location[1] - 1
                Dungeon.enter_room(self, Dungeon.location)
            else:
                print("Can't go any farther west.")
        else:
            print("Command not recognized, try again.")
  
class Action:
    get_item = ""
    use_item = ""
    def examine_room(self, noun):
        self.noun = noun
        if "table" in self.noun and "table" in Dungeon.text:
            if "sandwich" not in Player.inventory and "key" not in Player.inventory:
                print("There is a gently used sandwich on the table. Looks delicious?")
                Action.get_item = "sandwich"
            else:
                print("It looks like something square was recently removed from the table.")
                print("Oh yeah, that was you when you snagged that sandwich just moments ago.")
                print("What are you still doing in this room?")
        elif "chair" in self.noun and "chair" in Dungeon.text:
            print("It's a dang chair, {}. It has four legs and you use it for sitting.".format(Player.username))
            Action.get_item = "chair"
        elif "painting" in self.noun and "painting" in Dungeon.text:
            print("It's a very graphic painting involving what appears to be an affluent family auditioning for a talent agent.")
            Action.get_item = "painting"
        elif "man" in self.noun and "man" in Dungeon.text:
            if "key" not in Player.inventory:
                print('You get a closer look. He could use a bath. He is whispering "So hungry..." over and over.')
                Action.get_item = "chair"
                Action.use_item = "sandwich"
            else:
                print("He is happily munching away on a sandwich. He pauses between bites to give you a thumbs-up.")
        elif "lantern" in self.noun and "lantern" in Dungeon.text:
            if Dungeon.doors != "solved":
                print("The lantern appears to be a lever. Deep in your brain, a thought stirs.")
                print('"Hey, if you pull on this, something probably will happen."')
                Action.use_item = "lever"
            else:
                print("Once you solve a puzzle, it's not really fun any more, don't you think?")
                Action.use_item = "lever"
        elif "desk" in self.noun and "desk" in Dungeon.text:
            if "coins" not in Player.inventory and "drawing" not in Player.inventory:
                print("You see a pile of coins on the desk. Hey, free money!")
                Action.get_item = "coins"
            else:
                print("There are a few scattered coins left, but the desk is otherwise empty.")
                Action.get_item = "coins"
        elif "ghost" in self.noun and "ghost" in Dungeon.text:
            if "drawing" in Player.inventory:
                print("The ghost is holding pencil and paper, and seems to be working on another drawing.")
                print("It doesn't even notice you are in the room.")
                Action.get_item = "ghost"
            else:
                print("It's real spooky. It appears to be making a begging gesture.")
                Action.get_item = "ghost"
                Action.use_item = "coins"
        elif "ceiling" in self.noun and "ceiling" in Dungeon.text:
            print("What's your deal, {}? Do you have trouble focusing?".format(Player.username))
            print("The ghost looks up at the ceiling, too, confused by your sudden interest in non-ghost things.")
            Action.get_item = "ceiling"
        elif "crest" in self.noun and "crest" in Dungeon.text:
            if "sword" not in Player.inventory:
                print("The crest bears an image of dragons and unicorns fighting each other.")
                print("There's a pretty sick-looking sword attached to the bottom of the crest.")
                Action.get_item = "sword"
            else:
                print("You can definitely tell that the sword is missing from the crest.")
                print("You hope you are far away from here before anybody notices it's missing.")
        elif "door" in self.noun and "door" in Dungeon.text:
            print("The carvings on the door show people being torn apart by a monster. So metal.")
            print("This looks like it could be the way out of the dungeon.")
            print("You notice a keyhole in the center of the door.")
            Action.use_item = "key"
        else:
            print("Command not recognized, try again.")

    def get_something(self, noun):
        self.noun = noun
        if "sandwich" in self.noun and "sandwich" in Action.get_item:
            print("Hey, it's going to go bad anyway if it just sits here.")
            print("You put the sandwich in your inventory.")
            Player.inventory.append("sandwich")
            Action.get_item = ""
        elif "chair" in self.noun and "chair" in Action.get_item:
            print("What are you going to do with a chair?")
        elif "painting" in self.noun and "painting" in Action.get_item:
            print("Aw, dude, you've got a real twisted mind if you want to keep that.")
            print("It seems to be securely fastened to the wall, anyway. THANK GOODNESS.")
        elif "coins" in self.noun and "coins" in Action.get_item:
            if "coins" not in Player.inventory and "drawing" not in Player.inventory:
                print("You pick up a handful of golden coins.")
                print('They appear to be a form of currency called "Zorkmids."')
                print("Sounds fake to you. You put the worthless coins in your pocket anyway.")
                Player.inventory.append("coins")
            else:
                print("A handful of useless currency seems like enough. No need to be greedy.")
        elif "ghost" in self.noun and "ghost" in Action.get_item:
            print("You probably need to call somebody for that.")
        elif "ceiling" in self.noun and "ceiling" in Action.get_item:
            print('How, precisely, does one "get" a ceiling?')
            print("Honestly, sometimes I wonder if you're purposefully trying to break this game...")
        elif "sword" in self.noun and "sword" in Action.get_item:
            print("Aww yissss, you rip that sword off the wall and brandish it over your head like a ninja.")
            print("You don't realy know how to use a sword, but you know you look cool as hell.")
            print("You add the sword to your inventory. Mathematical!")
            Player.inventory.append("sword")
            Action.get_item = ""
        else:
            print("Command not recognized, try again.")

    def use_something(self, noun):
        self.noun = noun
        self.answer = ""
        if "lever" in self.noun and "lever" in Action.use_item:
            if Dungeon.doors != "solved":
                print("You pull down on the lantern and the walls hum to life.")
                print("You hear a series of clicking noises as the doors unlock.")
                print("You silently congratulate yourself on your ingenuity.")
                Dungeon.doors = "solved"
            else:
                print("Even though the doors are already unlocked, you pull the lever a few more times for fun.")
                print("Nothing happens, of course, and eventually you get bored and prepare to move on.")
        elif "sandwich" in self.noun and "sandwich" in Action.use_item:
            if "sandwich" in Player.inventory:
                print("You pull out the sandwich. The old man's eyes light up at the sight of such a tasty morsel.")
                print("He gestures for you to give him the sandwich. The temperature of the room suddenly drops 20 degrees.")
                print("And yet, you remember you haven't eaten anything all day, either. Why shouldn't you eat the sandwich?")
                print("Shivering slightly, you hold the sandwich before you. Do you (g)ive it to the old man, or (e)at it yourself?")
                self.answer = str.lower(input("> "))
                while True:
                    if self.answer == "g":
                        print("He does look awfully hungry, and the whole changing temperature thing is kind of freaking you out.")
                        print("You hand over the sandwich as your stomach grumbles in pain.")
                        print("The old man snatches the sandwich from your hand and tears into it with his rotting, yellow teeth.")
                        print("Not even looking at you, he pulls a rusted key from his pocket and tosses it your direction.")
                        print("You add the key to your inventory. Too bad you can't eat keys.")
                        Player.inventory.remove("sandwich")
                        Player.inventory.append("key")
                        break
                    elif self.answer == "e":
                        print("Yeah, screw the old man, you found that sandwich fair and square.")
                        print("You get right up in his gross, wrinkled face and take a big ol' bite of the sandwich.")
                        print("It tastes pretty dry, and it has pickles, which you hate, but the look on his face is worth it.")
                        print("The old man's mouth drops open, and he raises a fist above his head, which erupts with blue flame.")
                        print("You have just enough time to wonder at the old man's power before he burns you alive, sandwich and all.")
                        print("I hope you learned an important lesson about how old people might secretly be wizards.")
                        Player.quit_game()
                    else:
                        print("Command not recognized, try again.")
                    self.answer = str.lower(input("> "))
            else:
                print("You don't have any food on you.")
        elif "coins" in self.noun and "coins" in Action.use_item:
            if "coins" in Player.inventory and "drawing" not in Player.inventory:
                print("You shriek like a child and whip some Zorkmids at the ghost in fright.")
                print("They travel right through its incorporeal form, clattering against the wall behind it.")
                print("However, the ghost just nods at you and waves its arm.")
                print("A piece of paper floats down from the ceiling and you grab it out of the air.")
                print("It is a crude drawing of a house in a field of flowers. Great, everybody's an artist now.")
                print("You stuff the drawing in your inventory so as not to offend the ghost, which, again, is super spooky.")
                Player.inventory.append("drawing")
            elif "drawing" in Player.inventory:
                print("You throw a few more coins at the ghost for good measure, but it ignores you.")
        elif "key" in self.noun and "key" in Action.use_item:
            if "key" in Player.inventory:
                print("You insert Key A into Keyhole B like the talented monkey you are.")
                print("The key turns by itself in the lock and the doors slowly open.")
                Action.end_game(self)
            else:
                print("You don't have a key, dummy. Did you think it would be that easy?")
        else:
            print("Command not recognized, try again.")

    def end_game(self):
        self.answer = ""
        self.player_die1 = 0
        self.player_die2 = 0
        self.player_roll = 0
        self.demon_die1 = 0
        self.demon_die2 = 0
        self.demon_roll = 0
        print("You step through the doors and into the hallway on the other side.")
        print("Standing in the middle of the hallway, there shines a shiny demon.")
        print("The demon is blocking your way, but behind him you can see light from outside.")
        print("To try to pass the demon, you can:")
        if "drawing" in Player.inventory:
            print("Give the demon a (d)rawing to appeal to its softer side.")
        if "sword" in Player.inventory:
            print("Try to (f)ight the demon with your trusty sword you just found on a wall.")
        print("If you're feeling lucky and have a gambling problem, (p)lay a dice game against the demon.")
        print("Or you can duel the demon the old-fashioned way: with (m)usical insruments.")
        print("Make your choice, dear reader.")
        while True:
            self.answer = str.lower(input("> "))
            if self.answer == "d":
                if "drawing" in Player.inventory:
                    print("Like a true liberal arts major, you believe the pen is mightier than the sword.")
                    print("The demon raises its war hammer in a menacing pose as you approach.")
                    print("Trembling with fear, you pull out the ghost's drawing and sheepishly thrust it toward the demon.")
                    print("The demon lowers its hammer in shock, and then grabs the drawing from your hand.")
                    print("With tears brimming in its eyes and quickly burning away with a hiss,")
                    print("the demon cradles the precious drawing to its chest and steps aside to let you pass.")
                    print("Geez, what a giant baby. You run past the demon and out of the dungeon, victorious.")
                    print("Now on to your next adventure: finding a dang sandwich before you starve to death.")
                    Player.quit_game()
                else:
                    print("Command not recognized, try again.")
            elif self.answer == "f":
                if "sword" in Player.inventory:
                    print("Hell yes. It's all come down to this.")
                    print("You slowly approach the demon, furiously trying to shake something out of your shirt sleeve.")
                    print('The demon turns its head. "What could this be?" it wonders. "What could be in that sleeve?"')
                    print("You shake your sleeve even harder. You look down through the cuff where your hand should be.")
                    print("The demon beckons you forward and gestures for you to show him your sleeve.")
                    print("You shrug and offer him the empty cuff. He peers into the blackness, squinting in confusion.")
                    print("You thrust your sword out of the sleeve and into that terrifying idiot's eyeball. Nice move!")
                    print("The demon roars with pain and lashes out blindly. You easily duck its swing and run past.")
                    print("""You exit the dungeon victorious, singing Neil Diamond's "Sweet Caroline" at the top of your lungs.""")
                    Player.quit_game()
                else:
                    print("Command not recognized, try again.")
            elif self.answer == "p":
                print("Hmm, alright. The demon agrees to leave your fate to the dice.")
                self.player_die1 = random.randint(1, 6)
                self.player_die2 = random.randint(1, 6)
                self.player_roll = self.player_die1 + self.player_die2
                self.demon_die1 = random.randint(1, 6)
                self.demon_die2 = random.randint(1, 6)
                self.demon_roll = self.demon_die1 + self.demon_die2
                print("You roll first. You roll a {} and a {}. That makes {}!".format(self.player_die1, self.player_die2, self.player_roll))
                print("The demon rolls next. He rolls a {} and a {}. That makes {}!".format(self.demon_die1, self.demon_die2, self.demon_roll))
                if self.player_roll > self.demon_roll:
                    print("Nice one! The demon howls with rage as it is forced to let you pass.")
                    print("You can hardly believe the demon would honor such a stupid way to risk your life.")
                    print("And yet, you walk triumphantly out of the dungeon in one piece.")
                    print("Time to head to the nearest casino. Maybe you'll win enough money to buy a sandwich!")
                    Player.quit_game()
                elif self.player_roll == self.demon_roll:
                    print("What? You tied!? What are the odds? Seriously, you don't know, you're not good at math.")
                    print("You smirk at the demon as your execution is temporarily stayed.")
                    print("Looks like we're rolling again, sucker!")
                    print("But the demon has other plans. It's his rules, after all.")
                    print("He raises his giant war hammer and smashes it into your face.")
                    print("I suppose that's what you get for playing a game of chance with a demon.")
                    print("As you bleed out through your face holes, you can't help but wonder")
                    print("if there was a better way to handle that situation.")
                    Player.quit_game()
                else:
                    print("Uh oh, looks like you bet the farm and now you're going to lose the farm.")
                    print('And by "the farm," of course I mean "your life."')
                    print('And by "bet," of course I mean "foolishly wasted."')
                    print('And by "lose," of course I mean "this demon is going to wreck your vital organs."')
                    print('And by "uh oh," of course I mean "UH OH, you really screwed up this time."')
                    print("Anyway the demon kills you and that's the end of it.")
                    Player.quit_game()
            elif self.answer == "m":
                print("Haha, awesome. Classic demon battle rules.")
                print("The demon gives a respectful nod and slaps a hand against the corridor wall.")
                print("A panel slides back, revealing a recess filled with every instrument imaginable.")
                print("The old man appears behind you, half-eaten sandwich in hand.")
                print('"I shall judge the contest," he croaks. The demon lifts up his instrument of choice.')
                print("It's an antique wooden hurdy-gurdy worn by age and extensive use.")
                print("Of the myriad instruments available, there are only two you know how to play:")
                print('the theremin and the gong. Which do you choose? (Type "theremin" or "gong")')
                while True:
                    self.answer = str.lower(input("> "))
                    if self.answer == "theremin":
                        print("Where did you learn to play the theremin? Are you in a 70s progressive rock band?")
                        print("Anyway, the demon goes first. He's good. Like, REALLY good.")
                        print("He takes the hurdy-gurdy to heretofore unseen levels of awesomeness.")
                        print("After a few minutes of shredding, the demon stops with a flourish, breathing heavily.")
                        print("The old man seems impressed. Now it's your turn.")
                        print("You pour your heart out into the dumb poses you have to make with your hands and arms")
                        print("in order to play the theremin, and it responds with a chorus of high-pitched whining.")
                        print("You dance with the machine like you've never danced before, until finally you end on a triumphantly whiny note.")
                        print("The old man LOVES it, and quickly declares you the winner. The demon screams and smashes his hurdy-gurdy.")
                        print("You wave goodbye to the bested demon and exit the dungeon, victorious.")
                        Player.quit_game()
                    elif self.answer == "gong":
                        print("Um, okay. Even though it seems like a bad idea, you pick up a mallet and stand by your gong.")
                        print("The demon goes first. He's good. Like, REALLY good.")
                        print("Way better than any sound you could make on a gong, probably. You're starting to get nervous.")
                        print("After a few minutes of shredding, the demon stops with a flourish, breathing heavily.")
                        print("The old man seems impressed. Now it's your turn.")
                        print("You slam the mallet into the gong as hard as you can, then just stand there in silence.")
                        print("You hold this pose for three minutes as the gong reverberates, then bow to indicate the piece is over.")
                        print("""The old man says it's "just okay" and judges the demon to be the winner.""")
                        print("You throw your mallet at the demon as it approaches but it easily swats it aside.")
                        print("Then the demon eats you. Whoops! I guess you aren't as good of a gong player as you thought.")
                        Player.quit_game()
                    else:
                        print("Command not recognized, try again.")
            else:
                print("Command not recognized, try again.")

class Engine:
    """Runs the program"""
    prompt = ""
    def __init__(self, command):
        """Interprets the user's command"""
        Engine.prompt = command
        while True:
            if "move" in Engine.prompt:
                if Dungeon.doors != "locked":
                    Dungeon.move(self, Engine.prompt)
                else:
                    print("The doors are locked!")
            elif "examine" in Engine.prompt:
                Action.examine_room(self, Engine.prompt)
            elif "get" in Engine.prompt:
                Action.get_something(self, Engine.prompt)
            elif "use" in Engine.prompt:
                Action.use_something(self, Engine.prompt)
            elif Engine.prompt == "inventory":
                Player.check_inventory()
            elif Engine.prompt == "map":
                Player.check_map()
            elif Engine.prompt == "quit":
                Player.quit_game()
            elif Engine.prompt == "help":
                Player.show_help()
            else:
                print("Command not recognized, try again.")
            Engine.prompt = str.lower(input("> "))
        

print("Welcome to Brian's Zork-like!")
print("An adventure in learning and efficiency.")
user = Player(input("Enter your name to begin your adventure: "))
dungeon = Dungeon(3, 3, "roominfo.txt")
play = Engine(str.lower(input("> ")))
