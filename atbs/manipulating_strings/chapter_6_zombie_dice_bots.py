
# class MyZombie:
#     def __init__(self, name):
#         # All zombies must have a name:
#         self.name = name
#
#     def turn(self, gameState):
#         # gameState is a dictionary with info about the current state of the game.
#         # You can choose to ignore it in your code.
#
#         diceRollResults = zombiedice.roll() # first roll
#         # roll() returns a dictionary with keys 'brains', 'shotgun', and
#         # 'footsteps' with how many rolls of each type there were.
#         # The 'rolls' key is a list of (color, icon) tuples with the
#         # exact roll result information.
#         # Example of a roll() return value:
#         # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
#         #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
#         #            ('green', 'shotgun')]}
#
#         # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
#         brains = 0
#         while diceRollResults is not None:
#             brains += diceRollResults['brains']
#
#             if brains < 2:
#                 diceRollResults = zombiedice.roll() # roll again
#             else:
#                 break

