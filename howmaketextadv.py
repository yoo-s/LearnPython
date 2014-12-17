current_section = 0

sections = [
    (
"""You are at the front of your farmhouse. Your friend's house is to the
north, and the driveway to the southeast.  There is a mailbox here next to you.""",
    "Front Of Friend's House"), #0
    (
"""You are in your friend's house.  Stairs lead up to the west, the kitchen to the
north, and the living room to the east.  The exit is to the south.""",
    "Friend's House"), #1
#and so on
#23456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789["]
]

sec = {}
for indexed in enumerate(sections):
    index = indexed[0]
    long_name = indexed[1][1] # indexed[1][0] is the description
    short_name = ''
    for C in long_name:
        if C in ' /': # spaces and slashes to dashes
            short_name += '-'
        elif not C in ".'": # don't use periods and apostrophes
            short_name += C.lower() # lowercase
    sec[short_name] = index

dirs = {'north': 0, 'n': 0, 'south': 1, 's': 1,
        'west': 2, 'w': 2, 'east': 3, 'e': 3,
        'northeast': 4, 'ne': 4, 'southeast': 5, 'se': 5,
        'northwest': 6, 'nw': 6, 'southwest': 7, 'sw': 7,
        'up': 8, 'u': 8, 'down': 9, 'd': 9,
        'in': 10, 'out': 11, 'on': 10, 'off': 11,
        'enter': 10, 'exit': 11}

dungeon_map = [
#     n   s   e   w  ne  nw  se  sw  up  dn  in  out
    [ 1, 15, -1, -1, -1, -1, 15, -1, -1, -1,  1, -1], #0
    [ 2,  0,  3,  4, -1, -1, -1, -1,  4, -1, -1,  0], #1
# and so on.
]