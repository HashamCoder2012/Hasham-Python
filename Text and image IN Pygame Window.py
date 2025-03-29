import pygame
pygame.init()
screen_width,screen_height=500,500
display_surface=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Adding image text and background image')
background_image=pygame.transform.scale(
    pygame.image.load('C:/Users/Khurram shahzad.NAJIB-SMA/Desktop/Hasham Python/360_F_88981880_YjJManMJ6hJmKr5CZteFJAkEzXIh8mxW.jpg').convert(),
    (screen_width,screen_height)
)
penguin_image=pygame.transform.scale(
    pygame.image.load('C:/Users/Khurram shahzad.NAJIB-SMA/Documents/hassan work/360_F_644014899_W74ULTOVpJlCJmYACzv4qtR1X9QKx1qZ.jpg').convert_alpha(),

    (screen_width//2,screen_height//2)
)
penguin_rect=penguin_image.get_rect(center=(screen_width//2,screen_height//2))
text=pygame.font.Font(None,36).render('Hello world',True,pygame.Color('black'))
text_rect=text.get_rect(center=(screen_width//2,screen_height//2+110))
clock=pygame.time.Clock()
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    display_surface.blit(background_image,(0,0))
    display_surface.blit(penguin_image,penguin_rect)
    display_surface.blit(text,text_rect)
    pygame.display.flip()
    clock.tick(30)