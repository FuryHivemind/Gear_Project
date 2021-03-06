import pygame
from pygame.locals import *
from sys import exit


drone1 = "Drone1.png"
drone2 = "Drone2.png"
ybutton1 = "yButton1.png"
ybutton2 = "yButton2.png"

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Gear Project")
bg_image = "snow.png"


bg = pygame.image.load(bg_image).convert()

#Load Sprites
sprite1 = pygame.image.load(drone1)
sprite2 = pygame.image.load(drone2)
button1 = pygame.image.load(ybutton1)
button2 = pygame.image.load(ybutton2)


droneImage = 1
buttonImage = 1
x = 300
y = 250

speed_x = 133
speed_y = 170

#To play with time for animation
clock = pygame.time.Clock()



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()



    screen.blit(bg, (0, 0))

    time_passed = clock.tick(20)
    time_passed_seconds = time_passed / 1000.0

    x += speed_x * time_passed_seconds

#Animate Button 1
    if buttonImage == 1:
        screen.blit(button1, (10, 10))
    if buttonImage == 1:
        screen.blit(button2, (10, 10))
    if buttonImage == 2:
        buttonImage -= 1
    else:
        buttonImage += 1


#Animate Drone Sprite
    if droneImage == 1:
        screen.blit(sprite1, (x, y))

    if droneImage == 2:
        screen.blit(sprite2, (x, y))

    if droneImage == 2:
        droneImage -= 1

    else:
        droneImage += 1


    if x > 640 - sprite1.get_width():
        speed_x = - speed_x
        x = 640 - sprite1.get_width()
    elif x < 0:
        speed_x = -speed_x
        x = 0



    pygame.display.update()



