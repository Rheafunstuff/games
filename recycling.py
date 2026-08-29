import pgzrun
import random
WIDTH=600
HEIGHT=600
totallevels=7
startspeed=10
gameover=False
gamecomplete=False
currentlevel=1
non_recycleable=["plasticbag", "plasticwrap", "plasticbox", "bottle"]
items=[]
animations=[]
def draw():
    global items, currentlevel, gameover, gamecomplete
    screen.clear()
    screen.blit("savetheplanet", (0,0))
    if gameover:
        screen.draw.text("The game is over, try again later!", fontsize=20, center=(200, 80), color= "white")
    elif gamecomplete:
        screen.draw.text("Good job, you completed the game!", fontsize=20, center=(200, 80), color= "white")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items=makeitems(currentlevel)

def makeitems(number_of_extra_items):
    itemstocreate=optiontocreate(number_of_extra_items)
    newitems=createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return newitems

#getting the extra non recycleable items with the paper one
def optiontocreate(number_of_extra_items):
    itemstocreate = ["paperbag"] 
    for i in range(number_of_extra_items):
        random_option = random.choice(non_recycleable)
        itemstocreate.append(random_option)
    return itemstocreate

#using it to convert items into actors
def createitems(itemstocreate):
    new_items = []
    for item in itemstocreate:
        new_actor = Actor(item)


pgzrun.go()
