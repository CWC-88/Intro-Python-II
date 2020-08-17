from room import Room
from player import Player

# # Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),
#
#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),
#
#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),
#
#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),
#
#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    'secret': Room("Secret Room", "Your greediness has led to your demise. Deep in the secret room youll find a "
                                  "surprise"),
}


# # Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# #
# # Main
# #

# # Make a new player object that is currently in the 'outside' room.
# player_name = input("Give me your name")
player = Player("random", room['outside'])


# # Write a loop that:
# while True:
# #
# # * Prints the current room name
#     print(f'{player} You are in {player.currentRoom.name} {player.currentRoom.description}')

# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
#     player_input = input(f 'where shall we go? \n press w for west \n s for south \n e for East \n n for north \n q to quit:')
#     if player_input == 'q':
#         print("goodbye")
#         break

#     if player_input == 'n':
#         player = Player(player_name, room['foyer'])
#     else:
#         print("try another way")
#         if player_input == 's':
#         player = Player(player_name, room['outside'])
#         elif player_input == 'n':
#         player = Player(player_name, room['overlook'])
#         elif player_input == 'e':
#         player = Player(player_name, room['narrow'])
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.

# player_input = input(f 'where shall we go? \n press w for west \n s for south \n e for East \n n for north \n q to quit'):
while True:
  print(f'{player} You are in {player.currentRoom.name} {player.currentRoom.description}')
  player_input = input(f'where shall we go? \n press w for west \n s for south \n e for East \n n for north \n q to quit /n:')
  if player_input == 'q':
    print("goodbye")
    break

  if player_input == 'n':
      player.currentRoom = room[player.currentRoom].n_to

  # dirMap = {
  #     "n": "n_to",
  #     "s": "s_to",
  #     "e": "e_to",
  #     "w": "w_to"
  # }

# player.currentRoom = getattr(player.currentRoom, dirMap[player_input.lower()])

# else:
#     print("try another way")
#     # if player_input == 's':
#     #   player.currentRoom = Player( room['outside'])
#     # elif player_input == 'n':
#     #   player.currentRoom = Player( room['overlook'])
#     # elif player_input == 'e':
#     #   player = Player( room['narrow'])




















