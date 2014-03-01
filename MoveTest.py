## Testing a basic move command function for a Zork-like
# Remember to use str.lower() when user inputs a command

command = ""
width, height = 5, 5
# creates a list of 25 tuples representing coordinates in a 5-by-5 grid from (0, 0) to (4, 4)
# to start in the middle, begin game at location (2, 2) in grid (index 12)
coordinates = [(x, y) for x in range(width) for y in range(height)]
location = list(coordinates[12])

def check_location():
    print("Current location is: ", location)

def move(direction):
    if direction == "move north":
        if location[0] > 0:
            location[0] = location[0] - 1
        else:
            print("Can't go any farther north.")
    elif direction == "move south":
        if location[0] < height - 1:
            location[0] = location[0] + 1
        else:
            print("Can't go any farther south.")
    elif direction == "move east":
        if location[1] < width - 1:
            location[1] = location[1] + 1
        else:
            print("Can't go any farther east.")
    elif direction == "move west":
        if location[1] > 0:
            location[1] = location[1] - 1
        else:
            print("Can't go any farther west.")
    else:
        print("Command not recognized, try again.")


print("Welcome to the Move Simulator 2000!")
print('To move, type "move" with a cardinal direction.')
print('To check your location, type "location".')
print('To quit, type "quit".')

while command != "quit":
    command = str.lower(input("> "))
    if "move" in command:
        move(command)
    elif command == "location":
        check_location()
    elif command == "quit":
        break
    else:
        print("Command not recognized, try again.")
        
print("Thanks for playing!")
