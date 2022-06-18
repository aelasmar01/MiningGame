import pygame

pygame.init()

#Creating screen and initalizing screen size 800 x 600 pixels
screenMaxX = 800
screenMaxY = 600
screen = pygame.display.set_mode( (screenMaxX,screenMaxY) )

#Game Caption
pygame.display.set_caption("MotherLoad")
icon = pygame.image.load("pickaxe.png")
pygame.display.set_icon(icon)

#Starting Position, Player Img and the speed of the player while moving
PlayerImg = pygame.image.load("001-miner.png")
PlayerX = 370
PlayerY = 270
PlayerSpeed = 0.4
changeInPlayerX =0
changeInPlayerY =0
#Draws character
def Player(x,y):
    screen.blit(PlayerImg,(x,y))

#Game will only close if close button is pressed
programRunning = True


while programRunning == True:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                changeInPlayerX -= PlayerSpeed
                if PlayerX > screenMaxX-35:
                    PlayerX -= PlayerSpeed

            if event.key == pygame.K_RIGHT:
                changeInPlayerX += PlayerSpeed
                if PlayerX < 10:
                    PlayerX += PlayerSpeed

            if event.key == pygame.K_UP:
                changeInPlayerY -= PlayerSpeed
                if PlayerY > screenMaxY-50:
                    PlayerY -= 1

            if event.key == pygame.K_DOWN:
                changeInPlayerY += PlayerSpeed
                if PlayerY < 20:
                    PlayerY += 1


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                changeInPlayerX = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changeInPlayerY = 0

        if event.type == pygame.QUIT:
            programRunning = False

    if PlayerX >= 3 and PlayerX <= screenMaxX-30:
        PlayerX += changeInPlayerX

    if PlayerY >= 5 and PlayerY <= screenMaxY-35:
        PlayerY += changeInPlayerY

    screen.fill((0,255,175))
    Player(PlayerX,PlayerY)
    pygame.display.update()
