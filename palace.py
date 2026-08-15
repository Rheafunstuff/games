import pgzrun
import random
WIDTH=600
HEIGHT=600
Princess=Actor("princess")
Strawberry=Actor("strawberry")
Strawberry.pos=300, 300
Princess.pos=570, 130
score=0
gameover=False
def draw():
    screen.blit("sky", (0,0))
    Strawberry.draw()
    Princess.draw()
    screen.draw.text("SCORE : "+str(score), color="purple", topleft=(100, 100))
    if gameover:
        screen.fill("black")
        screen.draw.text("GAME OVER! Well Done. Your score was "+str(score), color="white", topleft= (100, 100))
def timer():
    global gameover
    gameover= True
def randommove():
    Strawberry.x=random.randint(100, 500)
    Strawberry.y=random.randint(100, 500)
def update():
    global score
    if keyboard.left:
        Princess.x-=5
    if keyboard.right:
        Princess.x+=5
    if keyboard.up:
        Princess.y-=5
    if keyboard.down:
        Princess.y+=5
    if  Princess.colliderect(Strawberry):
        randommove()
        score+=5
clock.schedule(timer, 10.0)
pgzrun.go()