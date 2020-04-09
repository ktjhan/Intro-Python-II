from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player("Tintin", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def playerkey(x):
    global p
    print(f'{p.name} is moving...')

    if (x == 'n') and(p.current_room.n_to != None):
        p.current_room = p.current_room.n_to
        print(f'{p.name} is moving north!')
    elif (x == 'e') and(p.current_room.e_to != None):
        p.current_room = p.current_room.e_to
        print(f'{p.name} is moving east!')
    elif (x == 's') and(p.current_room.s_to != None):
        p.current_room = p.current_room.s_to
        print(f'{p.name} is moving south!')
    elif (x == 'w') and(p.current_room.w_to != None):
        p.current_room = p.current_room.w_to
        print(f'{p.name} is moving east!')
    elif (x not in ['n', 'e', 's', 'w']):
        print(f'{p.name} is moving nowhere. Try again...!')
    else:
        print(f"{p.name} can't move")


running = True

while running == True:
    print(f'{p.name} is in {p.current_room.name}')
    x = input("[n] North, [e] East, [s] South, [w] West, [q] Quit")
    if (x == 'q'):
        exit(1)
    else:
        playerkey(x)
