import pgzrun
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("blue")
    w=90
    h=100
    for i in range (7):
        rectangle=Rect((200, 400), (w, h))
        screen.draw.rect(rectangle, "white")
        w-=10
        h+=20

pgzrun.go()