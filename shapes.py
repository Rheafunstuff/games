import pgzrun
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("black")
    rectangle=Rect((300, 300),(120, 200))
    screen.draw.rect(rectangle,"pink")
    screen.draw.filled_rect(rectangle, "yellow")
    screen.draw.circle((200, 400), 70, "purple")
    screen.draw.filled_circle((500, 350), 70, "pink")
    screen.draw.line( (210, 550), (400, 100), "blue")
    screen.draw.text("I have drawn some shapes and a line", (10, 50), color= "white", fontsize= 30)
pgzrun.go()