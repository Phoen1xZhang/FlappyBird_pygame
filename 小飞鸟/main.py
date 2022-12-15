import pygame,sys
import elements
import pygame.freetype

windowSize=width,height=800,600
global screen
BLACK=0,0,0


def initGame():
    global screen
    pygame.init()
    screen=pygame.display.set_mode(windowSize)
    pygame.display.set_caption('Flappy Bird')
    pygame.key.set_repeat(1,2)


def startTheGame():
    initGame()
    font = pygame.freetype.Font('/System/Library/Fonts/Supplemental/Chalkboard.ttc', 48)
    fontColor = 187, 255, 255
    clock=pygame.time.Clock()

    bird=elements.Bird(screen)

    pillarList=[]
    pillarList.append(elements.Pillar())
    pillarList.append(elements.Pillar())
    bird.setZeroSpeed()
    for pillar in pillarList:
        pillar.setZeroSpeed()
    gameStarted=False
    isInitilized=True
    font.render_to(screen, (60, 250), 'Press [SPACE] to start the game.', fgcolor=fontColor)

    while True:
        if gameStarted:
            bird.move(screen)
            pillarList[0].move(screen)
        if pillarList[0].getPosition()<=400:
            pillarList[1].move(screen)

        if pillarList[0].getPosition()+pillarList[0].width<0:
            pillarList.remove(pillarList[0])
            pillarList.append(elements.Pillar())

        for pillar in pillarList:
            if bird.touchPillar(pillar):
                bird.setZeroSpeed()
                for p in pillarList:
                    p.setZeroSpeed()
                font.render_to(screen,(100,250),'Oops! You ran into the pillar!',fgcolor=fontColor)
                font.render_to(screen,(90,320),'Press [R] to restart the game.',fgcolor=fontColor)
                gameStarted=False
                isInitilized=False


        if bird.touchGround():
            bird.setZeroSpeed()
            for p in pillarList:
                p.setZeroSpeed()
            font.render_to(screen, (50, 250), 'Oops! You dropped on the ground!', fgcolor=fontColor)
            font.render_to(screen, (90, 320), 'Press [R] to restart the game.', fgcolor=fontColor)
            gameStarted=False
            isInitilized=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if not gameStarted and isInitilized:
                        bird.setNegativeSpeed()
                        for p in pillarList:
                            p.setPositiveSpeed()
                        pygame.draw.rect(screen,BLACK,(60,250,750,100))
                        bird.draw(screen)
                        gameStarted=True
                    if bird.getSpeed()!=0:
                        bird.setNegativeSpeed()
                if not gameStarted:
                    if event.key==pygame.K_r:
                        screen.fill(BLACK)
                        pillarList.clear()
                        pillarList.append(elements.Pillar())
                        pillarList.append(elements.Pillar())
                        font.render_to(screen, (60, 250), 'Press [SPACE] to start the game.', fgcolor=fontColor)
                        isInitilized=True
                        bird.setInitPosition()

            if event.type==pygame.KEYUP:
                if bird.getSpeed()!=0:
                    bird.setPositiveSpeed()

        clock.tick(200)
        pygame.display.update()


if __name__ == '__main__':
    startTheGame()