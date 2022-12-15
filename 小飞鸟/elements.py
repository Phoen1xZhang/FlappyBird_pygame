import pygame
import random


class Bird:
    def __init__(self,screen):
        self.size=[30,30]
        self.location=[385,285]
        self.speed=1
        self.color=255,255,97
        self.image=pygame.image.load('小鸟.png')
        self.image=pygame.transform.scale(self.image,(self.size[0],self.size[1]))
        self.imageRect=self.image.get_rect()
        self.imageRect=self.imageRect.move(self.location[0],self.location[1])
        screen.blit(self.image,self.imageRect)
        self.screen=screen

    def setInitPosition(self):
        self.imageRect=self.imageRect.move(385-self.location[0],285-self.location[1])
        self.location=[385,285]
        self.screen.blit(self.image,self.imageRect)

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.location[0],self.location[1],self.size[0],self.size[1]))

    def move(self,screen):
        BLACK=0,0,0
        pygame.draw.rect(screen, BLACK, (self.location[0], self.location[1], self.size[0], self.size[1]))
        if self.location[1]==0 and self.speed<0:
            self.speed=-self.speed
        self.location[1]+=self.speed
        # pygame.draw.rect(screen, self.color, (self.location[0], self.location[1], self.size[0], self.size[1]))
        self.imageRect=self.imageRect.move(0,self.speed)
        screen.blit(self.image,self.imageRect)

    def setNegativeSpeed(self):
        self.speed=-1

    def setPositiveSpeed(self):
        self.speed=1

    def setZeroSpeed(self):
        self.speed=0

    def getPosition(self):
        return self.location[0]

    def getSpeed(self):
        return self.speed

    def touchPillar(self,pillar):
        if self.location[0]+self.size[0]==pillar.getPosition() and (self.location[1]<=pillar.getupPillarHeight() or
           self.location[1]>=pillar.getupPillarHeight()+pillar.getGapHeight()-self.size[1]):
            return True
        if self.location[0]==pillar.getPosition()+pillar.getWidth():
            if self.location[1]<=pillar.getupPillarHeight() or self.location[1]>=pillar.getupPillarHeight()+pillar.getGapHeight()-self.size[1]:
                return True
        if pillar.getPosition()-self.size[0]<self.location[0]<pillar.getPosition()+pillar.getWidth():
            if self.location[1]==pillar.getupPillarHeight() or self.location[1]+self.size[1]==pillar.getupPillarHeight()+pillar.getGapHeight():
                return True
        return False

    def touchGround(self):
        if self.location[1]+self.size[1]==pygame.display.Info().current_h:
            return True
        return False


class Pillar:
    def __init__(self):
        self.width=70
        self.color=27,190,72
        self.position=[pygame.display.Info().current_w,0]
        self.upPillarHeight=random.randint(150,400)
        self.gapHeight=random.randint(80,150)
        self.downPillarHeight=pygame.display.Info().current_h-self.upPillarHeight-self.gapHeight
        self.speed=1

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.position[0],self.position[1],self.width,self.upPillarHeight))
        pygame.draw.rect(screen,self.color,(self.position[0],self.position[1]+self.upPillarHeight+self.gapHeight,self.width,self.downPillarHeight))

    def move(self,screen):
        BLACK=0,0,0
        pygame.draw.rect(screen,BLACK,(self.position[0],self.position[1],self.width,self.upPillarHeight))
        pygame.draw.rect(screen,BLACK,(self.position[0],self.position[1]+self.upPillarHeight+self.gapHeight,self.width,self.downPillarHeight))
        self.position[0]-=self.speed
        pygame.draw.rect(screen,self.color,(self.position[0],self.position[1],self.width,self.upPillarHeight))
        pygame.draw.rect(screen,self.color,(self.position[0],self.position[1]+self.upPillarHeight+self.gapHeight,self.width,self.downPillarHeight))

    def getPosition(self):
        return self.position[0]

    def getupPillarHeight(self):
        return self.upPillarHeight

    def getGapHeight(self):
        return self.gapHeight

    def getWidth(self):
        return self.width

    def setZeroSpeed(self):
        self.speed=0

    def setPositiveSpeed(self):
        self.speed=1