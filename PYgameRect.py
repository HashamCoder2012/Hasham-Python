import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,225),pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,(100,100,110),(300,150),50,3)
    pygame.draw.circle(screen,(100,100,110),(30,150),50)
    pygame.display.flip()
