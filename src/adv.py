from room import Room
from player import Player
from Fortuna import d

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
    'dragon_lair': Room("Dragon's Liar",
    "You're engulfed in flames as the ancient dragon's breath fills the room.")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].n_to = room['dragon_lair']
room['dragon_lair'].s_to = room['overlook']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Pyewacket', location=room['outside'])
print(f"\n{player.name}'s starting location: {player.location.name}")
print(f"{player.location.description}")


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

while True:
    direction_dispatch = {
    'n': lambda x: x.n_to,
    's': lambda x: x.s_to,
    'e': lambda x: x.e_to,
    'w': lambda x: x.w_to,
    }
    user_input = input("\nWhere would you like to go next?")
    if not user_input:
        continue
    else:
        user_input = user_input[0].lower()
    if user_input == 'q':
        exit()
    if user_input in direction_dispatch.keys():
        target = direction_dispatch[user_input](player.location)
        if target:
            player.location = target
            if target.name != "Dragon's Liar":
                print(f'{player.name} enters the {player.location.name}')
                print(f'{player.location.description}')
            else:
                if d(20) > 15:
                    print(f'{player.name} enters the {player.location.name}')
                    print(f'{player.location.description}')
                    print('You have been incinerated!')
                else:
                    print("You attempt to gain entry to the Dragon's Lair,\n"
                    "but fall to your death crossing the chasm.")
                exit()
        else:
            print("You cannot go that way!")
    else:
        print(f"You cannot go that way, '{user_input}' is not a valid "
        f"direction.\nTry one of these: (n,s,e,w)")
