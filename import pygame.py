import pygame
pygame.init()
sprite_color_change_event=pygame.USEREVENT+1
yellow=pygame.color('yellow')
green=pygame.color('green')
blue=pygame.color('blue')
black=pygame.color('black')

screen=pygame.display.set_mode((300,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==sprite_color_change_event:
            sp1.change_color()
    pygame.draw.rect(screen,(0,125,225),pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,(100,100,110),(200,150),50,3)
    pygame.draw.circle(screen,(100,100,110),(30,150),50)
    pygame.display.flip()
