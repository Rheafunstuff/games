import pgzrun
import random
WIDTH=600
HEIGHT=600
Fish=Actor("fish")
Shark=Actor("shark")
Fish.pos=300, 300
Shark.pos=570, 130
score=0
gameover=False
def draw():
    screen.blit("ocean", (0,0))
    Fish.draw()
    Shark.draw()
    screen.draw.text("SCORE : "+str(score), color="white", topleft=(100, 100))
    if gameover:
        screen.fill("black")
        screen.draw.text("GAME OVER! Well Done. Your score was "+str(score), color="white", topleft= (100, 100))
def timer():
    global gameover
    gameover= True
def randommove():
    Fish.x=random.randint(100, 500)
    Fish.y=random.randint(100, 500)
def update():
    global score
    if keyboard.left:
        Shark.x-=5
    if keyboard.right:
        Shark.x+=5
    if keyboard.up:
        Shark.y-=5
    if keyboard.down:
        Shark.y+=5
    if  Shark.colliderect(Fish):
        randommove()
        score+=5
clock.schedule(timer, 10.0)
pgzrun.go()