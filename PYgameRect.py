import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,225),pygame.Rect(30,30,60,60))
    pygame.draw.circle(screen,(100,100,110),(250,150),50,3)
    pygame.draw.circle(screen,(100,100,110),(30,150),50)
    pygame.display.flip()
    import pygame
import random


pygame.init()


SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1





YELLOW = pygame.Color('yellow')
GREEN = pygame.Color('green')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

# Sprite class representing the moving object
class Sprite(pygame.sprite.Sprite):

  # Constructor method
  def __init__(self, color, height, width):
    # Call to the parent class (Sprite) constructor
    super().__init__()
    # Create the sprite's surface with dimensions and color
    self.image = pygame.Surface([width, height])
    self.image.fill(color)
    # Get the sprite's rect defining its position and size
    self.rect = self.image.get_rect()
    # Set initial velocity with random direction
    self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

  # Method to update the sprite's position
  def update1(self):
    # Move the sprite by its velocity
    self.rect.move_ip(self.velocity)
    # Flag to track if the sprite hits a boundary
    boundary_hit = False
    # Check for collision with left or right boundaries and reverse direction
    if self.rect.left <= 0 or self.rect.right >= 500:
      self.velocity[0] = -self.velocity[0]
      boundary_hit = True
    # Check for collision with top or bottom boundaries and reverse direction
    if self.rect.top <= 0 or self.rect.bottom >= 400:
      self.velocity[1] = -self.velocity[1]
      boundary_hit = True

    # If a boundary was hit, post events to change colors
    if boundary_hit:
      pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
      

  # Method to change the sprite's color
  def change_color(self):
    self.image.fill(random.choice([YELLOW, GREEN, ORANGE, WHITE]))

all_sprites_list = pygame.sprite.Group()
# Instantiate the sprite
sp1 = Sprite(WHITE, 20, 30)
# Randomly position the sprite
sp1.rect.x = 0
sp1.rect.y =0
# Add the sprite to the group
all_sprites_list.add(sp1)

# Create the game window
screen = pygame.display.set_mode((500, 400))
# Set the window title

# Set the initial background color

# Apply the background color
screen.fill(GREEN)

# Game loop control flag
exit = False
# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Main game loop
while not exit:
  # Event handling loop
  for event in pygame.event.get():
    # If the window's close button is clicked, exit the game
    if event.type == pygame.QUIT:
      exit = True
    # If the sprite color change event is triggered, change the sprite's color
    elif event.type == SPRITE_COLOR_CHANGE_EVENT:
      sp1.change_color()
    # If the background color change event is triggered, change the background color
  all_sprites_list.update1()
  # Fill the screen with the current background color
  screen.fill(WHITE)
  # Draw all sprites to the screen
  all_sprites_list.draw(screen)
# Refresh the display
  pygame.display.flip()
  # Limit the frame rate to 240 fps
  clock.tick(240)

# Uninitialize all pygame modules and close the window
pygame.quit()
