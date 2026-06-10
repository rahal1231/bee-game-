import pgzrun
import random
WIDTH=1000
HEIGHT=1000
ship=Actor("ship")
ship.pos=(WIDTH/2,HEIGHT-60)
speed=5
bullets=[]
enymeis=[]
for i in range(10):
    for j in range(4):
        enymeis.append(Actor("bee"))
        enymeis[-1].x=100+50*i
        enymeis[-1].y=-80+50*j
score=0
derection=1
ship.dead=False
ship.countdown=90
def game_over():
    screen.draw.text("gaem over",(500,500))

def on_key_down(key):
    if ship.dead==False:
        if key==keys.SPACE:
            bullets.append(Actor("bullet"))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y -50
def update():
    global score,derection
    move_down=False
    if ship.dead==False:
        if keyboard.left:
            ship.x-=speed
            if ship.x<=0:
                ship.x=0
        if keyboard.right:
            ship.x+=speed
            if ship.x>=WIDTH:
                ship.x=WIDTH
    for i in bullets:
        if i .y<=0:
            bullets.remove(i)
        else:
            i.y-=10
    if len(enymeis)==0:
        game_over()
    if len(enymeis)>0 and (enymeis[-1].x>WIDTH-80 or enymeis[0].x<80):
        move_down=True
        derection=derection*-1
    for i in enymeis:
        i.x+=5*derection
        if move_down==True:
            i.y+=100
        if i.y>HEIGHT:
            enymeis.remove(i)
        for j in bullets:
            if i .colliderect(j):
                score+=100
                bullets.remove(j)
                enymeis.remove(i)
                if len (enymeis)==0:
                    game_over()
        if i.colliderect(ship):
            ship.dead=True
    if ship.dead:
        ship.countdown-=1
    if ship.countdown==0:
        ship.dead=False
        ship.countdown=90
def draw():
    screen.clear()
    screen.fill("blue")
    for i in bullets:
        i.draw()
    for i in enymeis:
        i.draw()
    ship.draw()
    screen.draw.text(str(score),(50,30))
    if len(enymeis)==0:
        game_over()

pgzrun.go()






