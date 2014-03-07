## Testing a basic move command function for a Zork-like
# Remember to use str.lower() when user inputs a command

command = ""
get_item = ""
use_item = ""
inventory = []
doors = "unlocked"
width, height = 5, 5
# creates a list of 25 tuples representing coordinates in a 5-by-5 grid from (0, 0) to (4, 4)
# to start in the middle, begin game at location (2, 2) in grid (index 12)
coordinates = [(x, y) for x in range(width) for y in range(height)]
# If width, height are not odd and same value this is going to get screwy
center = int((width * height - 1) / 2)
location = list(coordinates[center])

# Reads from a text file of room information and inputs it into a dictionary
# where key is location tuple and value is a string of room information
with open("roominfo.txt", "rt") as f:
    roominfo = f.read()
roomlist = roominfo.split("\n")
i = iter(roomlist)
roomkey = dict(zip(i, i))


def check_location():
    print("Current location is: ", location)

def check_inventory():
    print("Current inventory is: ", inventory)

def move(direction):
    if direction == "move north":
        if location[0] > 0:
            location[0] = location[0] - 1
            enter_room(location)
        else:
            print("Can't go any farther north.")
    elif direction == "move south":
        if location[0] < height - 1:
            location[0] = location[0] + 1
            enter_room(location)
        else:
            print("Can't go any farther south.")
    elif direction == "move east":
        if location[1] < width - 1:
            location[1] = location[1] + 1
            enter_room(location)
        else:
            print("Can't go any farther east.")
    elif direction == "move west":
        if location[1] > 0:
            location[1] = location[1] - 1
            enter_room(location)
        else:
            print("Can't go any farther west.")
    else:
        print("Command not recognized, try again.")
    return location

# Display text for new room
def enter_room(room):
    x = str(room[0])
    y = str(room[1])
    print(roomkey[x+y])
    if "locking" in roomkey[x+y]:
        global doors
        doors = "locked"

def examine(noun):
    x = str(location[0])
    y = str(location[1])
    if "desk" in noun and "desk" in roomkey[x+y]:
        print("You see a pile of coins on the desk. Hey, free money!")
        global get_item
        get_item = "coins"
    elif "lantern" in noun and "lantern" in roomkey[x+y]:
        print("The lantern appears to be a lever. Deep in your brain, a thought stirs.")
        print('"Hey, I think if you pull on this, something will happen."')
        global use_item
        use_item = "lever"
    else:
        print("Command not recognized, try again.")

def get(noun):
    x = str(location[0])
    y = str(location[1])
    if "coins" in noun and "coins" in get_item:
        print("You pick up a handful of golden coins.")
        print('They appear to be a form of currency called "Zorkmids."')
        print("Sounds fake to you. You put the worthless coins in your pocket anyway.")
        inventory.append("coins")
    else:
        print("Command not recognized, try again.")

def use(noun):
    x = str(location[0])
    y = str(location[1])
    if "lever" in noun and "lever" in use_item:
        print("You pull down on the lantern and the walls hum to life.")
        print("You hear a series of clicking noises as the doors unlock.")
        print("You silently congratulate yourself on your ingenuity.")
        global doors
        doors = "unlocked"
    else:
        print("Command not recognized, try again.")
        

print("Welcome to the Move Simulator 2000!")
print('To move, type "move" with a cardinal direction.')
print('To check your location, type "location".')
print('To check your inventory, type "inventory".')
print('To examine something, type "examine" with a noun.')
print('To get something, type "get" with a noun.')
print('To use an item, type "use" with a noun or something from your inventory.')
print('To quit, type "quit".')

while command != "quit":
    command = str.lower(input("> "))
    if "move" in command:
        if doors == "unlocked":
            move(command)
            get_item = ""
            use_item = ""
        else:
            print("The doors are locked!")
            continue
    elif command == "location":
        check_location()
    elif command == "inventory":
        check_inventory()
    elif "examine" in command:
        examine(command)
    elif "get" in command:
        get(command)
    elif "use" in command:
        use(command)
    elif command == "quit":
        break
    else:
        print("Command not recognized, try again.")
        
print("Thanks for playing!")
