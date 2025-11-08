import pygame
pygame.init()
width=500
height=500
screen=pygame.display.set_mode((300,500))
x=100
y=100
rectwidth=50
rectheght=50
x2=200
y2=200
rectwidth2=70
rectheght2=80
doone=False
while not doone:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
    press=pygame.key.get_pressed()
    if press[pygame.K_LEFT]: x=x-1
    if press[pygame.K_RIGHT]: x=x+1
    if press[pygame.K_UP]:y=y-1
    if press[pygame.K_DOWN]:y=y+1
    x=min(max(0,x),width-rectwidth)
    screen.fill((0,0,0))
    y=min(max(0,y),height-rectheght)
    pygame.draw.rect(screen,"Orange",pygame.Rect(x,y,rectwidth,rectheght))
    pygame.draw.rect(screen,"red",pygame.Rect(x2,y2,rectwidth2,rectheght2))
    pygame.display.flip()