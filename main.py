import pygame

pygame.init()

#Creating screen and initalizing screen size 800 x 600 pixels
screen = pygame.display.set_mode( (800,600) )

#Game Caption
pygame.display.set_caption("MotherLoad")
icon = pygame.image.load("pickaxe.png")
pygame.display.set_icon(icon)

PlayerImg = pygame.image.load("001-miner.png")
PlayerX = 370
PlayerY = 270

def Player():
    screen.blit(PlayerImg,(PlayerX,PlayerY))

#Game will only close if close button is pressed
programRunning = True
while programRunning == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programRunning = False

    screen.fill((0,255,175))
    Player()
    pygame.display.update()