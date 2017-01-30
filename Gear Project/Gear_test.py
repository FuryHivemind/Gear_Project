import pygame
from pygame.locals import *
from sys import exit


drone1 = "Drone1.png"
drone2 = "Drone2.png"

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Gear Project")
bg_image = "snow.png"


bg = pygame.image.load(bg_image).convert()

#Load Sprites
sprite1 = pygame.image.load(drone1)
sprite2 = pygame.image.load(drone2)

droneImage = 1
x = 40
y = 40


#To play with time for animation
clock = pygame.time.Clock()



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(bg, (0, 0))

    if droneImage == 1:

        screen.blit(sprite1, (x, y))

    if droneImage == 2:

        screen.blit(sprite2, (x, y))

    if droneImage == 2:

        droneImage -= 1

    else:
        droneImage += 1

    if x < 640:
        x += 1
    elif x == 640:
        x -= 640

    clock.tick(40)

    pygame.display.update()



