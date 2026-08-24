import pgzrun
import random
import time
WIDTH=600
HEIGHT=600
Clouds=[]
Lines=[]
NextCloud=0
TotalClouds=7
StartTime=0
EndTime=0
TotalTime=0
def createclouds():
    global StartTime
    for i in range(TotalClouds):
        Cloud=Actor("cloud")
        Cloud.pos=random.randint(100, 500), random.randint(100, 500)
        Clouds.append(Cloud)
    StartTime=time.time()
def draw():
    global TotalTime
    screen.blit("pinksky", (0,0))
    number=1
    for i in Clouds:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+30))
        i.draw()
        number+=1
    for i in Lines:
        screen.draw.line(i[0], i[1], "white")
    if NextCloud<TotalClouds:
        TotalTime=time.time()-StartTime
        screen.draw.text(str(round(TotalTime, 1)), (10, 10), fontsize=30)
    else:
        screen.draw.text(str(round(TotalTime, 1)), (10, 10), fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global NextCloud, Lines
    if NextCloud<TotalClouds:
        if Clouds[NextCloud].collidepoint(pos):
            if NextCloud:
                Lines.append((Clouds[NextCloud-1].pos,Clouds[NextCloud].pos))
            NextCloud+=1
        else:
            Lines=[]
            NextCloud=0
createclouds()
pgzrun.go()