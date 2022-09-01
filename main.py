# Task:
# Remember that tricky practice task, that we had last fifth lection?
# Great! So, you should make it little bit more user-friendly, like show only the result of work.
# For now, script shows all his journey, including wrong path passed on the screen step-by-step.
# You should make it show only the picture with the answer path. That's all!

# Self-review:
# Well, you'll see only one picture with right pass to exit. Nothing more, nothing less.

# Additional points:
# I don't think, that you'll ever need additional lists, sets, tuples or dictionaries.
# Everything you need is already in the script.

import sys
import time

map = [
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

def showMap():
    print()
    for row in map:
        for item in row:
            print (item, end="")
        print()

def action(x,y):
    if map[y][x] == 2:
        showMap()           # The function "showMap()" was added.
        print ("FINISHED!")
        sys.exit()
    if map[y][x] == 0:
        map[y][x] = "*"
        time.sleep(0.5)
        AI(x,y)

def AI(x,y):
    # showMap()       # The function was commented.
    action(x+1, y)
    action(x-1, y)
    action(x, y+1)
    action(x, y-1)

AI(5,3)