import pgzrun
import random
import time
WIDTH=600
HEIGHT=600
Stars=[]
Lines=[]
NextStar=0
TotalStars=7
StartTime=0
EndTime=0
TotalTime=0
def createstars():
    global StartTime
    for i in range(TotalStars):
        Star=Actor("star")
        Star.pos=random.randint(100, 500), random.randint(100, 500)
        Stars.append(Star)
    StartTime=time.time()
def draw():
    global TotalTime
    screen.blit("space", (0,0))
    number=1
    for i in Stars:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+30))
        i.draw()
        number+=1
    for i in Lines:
        screen.draw.line(i[0], i[1], "white")
    if NextStar<TotalStars:
        TotalTime=time.time()-StartTime
        screen.draw.text(str(round(TotalTime, 1)), (10, 10), fontsize=30)
    else:
        screen.draw.text(str(round(TotalTime, 1)), (10, 10), fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global NextStar, Lines
    if NextStar<TotalStars:
        if Stars[NextStar].collidepoint(pos):
            if NextStar:
                Lines.append((Stars[NextStar-1].pos, Stars[NextStar].pos))
            NextStar+=1
        else:
            Lines=[]
            NextStar=0
createstars()
pgzrun.go()