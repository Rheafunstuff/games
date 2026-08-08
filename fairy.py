import pgzrun
import random
WIDTH=600
HEIGHT=600
fairy=Actor("fairypicture")
fairy.pos=(300, 300)
message=""
def draw():
    screen.fill("sky blue")
    fairy.draw()
    screen.draw.text(message, (170, 75), fontsize=40)
def update():
    if keyboard.left:
        fairy.x-=5
    if keyboard.right:
        fairy.x+=5
    if keyboard.up:
        fairy.y-=5
    if keyboard.down:
        fairy.y+=5
def mouse():
    fairy.x=random.randint(100, 500)
    fairy.y=random.randint(100, 500)
def on_mouse_down(pos):
    global message
    if fairy.collidepoint(pos):
        mouse()
        message="Good Job!"
    else:
        message="Nice try, but not quite!"
pgzrun.go()