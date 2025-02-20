import sys, pygame
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode((200, 200))
CLOCK  = pygame.time.Clock()

# Wrong, the box doesn't rotate it just gets bigger/smaller
# surface = pygame.Surface((50 , 50))

# Method 1
surface = pygame.Surface((50 , 50), SRCALPHA)

# Method 2
# surface = pygame.Surface((50 , 50))
# RED = (255, 0 , 0)
# surface.set_colorkey(RED)

surface.fill((0, 0, 0))
rotated_surface = surface
rect = surface.get_rect()
angle = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((255, 255, 255))
    angle += 5
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect(center = (100, 100))
    SCREEN.blit(rotated_surface, (rect.x, rect.y))
    # same thing
    # SCREEN.blit(rotated_surface, rect)
    pygame.display.update()
    CLOCK.tick(30)