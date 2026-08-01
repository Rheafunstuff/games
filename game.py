import pgzrun
import random
WIDTH=600
HEIGHT=600
spaceship=Actor("spaceship")
spaceship.pos=(300, 300)
message=""
def draw():
    screen.fill("black")
    spaceship.draw()
    screen.draw.text(message, (300, 75), fontsize=40)
def update():
    if keyboard.left:
        spaceship.x-=10
    if keyboard.right:
        spaceship.x+=10
    if keyboard.up:
        spaceship.y-=10
    if keyboard.down:
        spaceship.y+=10
def mouse():
    spaceship.x=random.randint(100, 500)
    spaceship.y=random.randint(100, 500)
def on_mouse_down(pos):
    global message
    if spaceship.collidepoint(pos):
        mouse()
        message="Good Job!"
    else:
        message="Nice try, but not quite!"
pgzrun.go()