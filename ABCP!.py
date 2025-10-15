import pygame
import random
pygame.init()
screen=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Colour Changing Sprites")
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
colors=[red, green, blue, yellow]
current_color1=random.choice(colors)
current_color2=random.choice(colors)
sprite1=pygame.Rect(100, 120, 50, 50)
sprite2=pygame.Rect(250, 120, 50, 50)
CHANGE_COLOR=pygame.USEREVENT+1
pygame.time.set_timer(CHANGE_COLOR, 2000)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==CHANGE_COLOR:
            current_color1=random.choice(colors)
            current_color2=random.choice(colors)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen,current_color1,sprite1)
    pygame.draw.rect(screen,current_color2,sprite2)
    pygame.display.flip()
pygame.quit()