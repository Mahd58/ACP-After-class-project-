import pygame
pygame.init()
screen=pygame.display.set_mode((700,500))
font=pygame.font.SysFont("Arial", 40)
text=font.render("I am the best student of the term!",True,(255,255,255))
screen.blit(text,(20,20))
donne=False
while not donne:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            donne=True
    pygame.draw.rect(screen,"blue",pygame.Rect(120,120,30,40))
    pygame.draw.circle(screen,"orange",(100,90),50,5)
    pygame.display.flip()
