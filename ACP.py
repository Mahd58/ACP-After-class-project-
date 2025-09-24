import pygame
pygame.init()
screen=pygame.display.set_mode((500,300))
pygame.display.set_caption("My first GAME SCREEN")
image=pygame.transform.scale(
    pygame.image.load("Cool nebula.jpeg").convert(),
    (500,300)
)
close_screeen=False
while not close_screeen:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(image,(0,0))
    pygame.display.flip()
pygame.quit()