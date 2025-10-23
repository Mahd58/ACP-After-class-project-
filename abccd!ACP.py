# Write a program to create a Space Invader Game using Pygame Library in Python.
import math
import random
import pygame
# Constants
Screen_width=800
Screen_height=500
player_start_X=370
player_start_Y=380
Enemy_start_Y_min=50
Enemy_start_Y_max=150
Enemy_speed_y=4
Fireball_speed_y=10
Enemy_speed_x=1
Collision_distance=27
pygame.init()
pygame.mixer.init()
Screen=pygame.display.set_mode((Screen_width,Screen_height))
pygame.display.set_caption("Space invader")
icon=pygame.image.load("Rocket.png")
pygame.display.set_icon(icon)
player_image = pygame.transform.scale(pygame.image.load('Rocket.png'), (64, 64))

fireball_image = pygame.transform.scale(pygame.image.load('fireball.png'), (32, 32))
#player_image=pygame.image.load("Rocket.png")
player_x=player_start_X
player_y=player_start_Y
player_x_change=0
enemy_image=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
number_of_enemies=5
for i in range(0,number_of_enemies):
    #alien_image=pygame.image.load("alien.png")
    enemy_image.append(pygame.transform.scale(pygame.image.load('alien.png'), (50, 50)))
    #enemy_image.append(alien_image)
    enemy_x.append(random.randint(0,Screen_width-64))
    enemy_y.append(random.randint(Enemy_start_Y_min,Enemy_start_Y_max))
    enemy_x_change.append(Enemy_speed_x)
    enemy_y_change.append(Enemy_speed_y)
#fireball_image=pygame.image.load("fireball.png")
fireball_x=0
fireball_y=player_start_Y
fireball_x_change=0
fireball_y_change=Fireball_speed_y
fireball_state="ready"
close_screen=False
bg=pygame.image.load("The-stars.webp")
bg=pygame.transform.scale(bg,(Screen_width,Screen_height))
# score
score=0
font=pygame.font.Font(None,40)
scorex=20
scorey=20
# game over
game_over=pygame.font.Font(None,60)
def show_score(x,y):
    points=font.render("score = "+str(score),True,(255,255,255))
    Screen.blit(points,(x,y))
def show_game_over():
    text=game_over.render("GAME OVER",True,(255,0,0))
    Screen.blit(text,(250,250))
def player(x,y):
    Screen.blit(player_image,(x,y))
def enemy(x,y,i):
    Screen.blit(enemy_image[i],(x,y))
def fireball(x,y):
    global fireball_state
    fireball_state="fire"
    Screen.blit(fireball_image,(x+10,y+6))
def collision(firebally,fireballx,enemyx,enemyy):
    distance=math.sqrt((enemyx-fireballx)**2+(enemyy-firebally)**2)
    return distance<Collision_distance
while not close_screen:
    Screen.fill((0,0,0))
    Screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_x_change=-5
            if event.key==pygame.K_RIGHT:
                player_x_change=5
            if event.key==pygame.K_SPACE and fireball_state=="ready":
                fireball_x=player_x
                fireball(fireball_x,fireball_y)
    # player movement
    player_x=player_x+player_x_change
    player_x=max(0,min(player_x,Screen_width-64))
    # enemy movement
    for i in range(5):
        if enemy_y[i]>340:
            for j in range(5):
                enemy_y[i]=2000
            show_game_over()
            break
        enemy_x[i]=enemy_x[i]+enemy_x_change[i]
        if enemy_x[i]<0 or enemy_x[i]>=Screen_width-64:
            enemy_x_change[i]*=-1
            enemy_y[i]+=enemy_y_change[i]
        if collision(fireball_y,fireball_x,enemy_x[i],enemy_y[i]):
            fireball_y=player_y
            fireball_state="ready"
            score=score+1
            enemy_x[i]=random.randint(0,Screen_width-64)
            enemy_y[i]=random.randint(Enemy_start_Y_min,Enemy_start_Y_max)
        enemy(enemy_x[i],enemy_y[i],i)
    if fireball_y<0:
        fireball_y=player_start_Y
        fireball_state="ready"
    elif fireball_state=="fire":
        fireball(fireball_x,fireball_y)
        fireball_y-=fireball_y_change
    player(player_x,player_y)
    show_score(scorex,scorey)
    pygame.display.flip()
pygame.quit()
