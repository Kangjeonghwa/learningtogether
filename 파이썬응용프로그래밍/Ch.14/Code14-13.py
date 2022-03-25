import pygame
import random
import sys

from pygame.constants import K_LEFT

def paintEntity(entity,x,y):
    monitor.blit(entity,(x,y))


def playGame():
    global monitor, ship, monster, missile

    r=random.randrange(0,256)
    g=random.randrange(0,256)
    b=random.randrange(0,256)
    
    shipX=swidth/2
    shipY=sheight*0.8
    dx,dy=0,0

    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize=monster.get_rect().size
    monsterX=0
    monsterY=random.randrange(0,int(swidth*0.3))
    monsterSpeed=random.randrange(1,5)

    missileX, missileY=None,None

    while True:
        (pygame.time.Clock()).tick(50)
        monitor.fill((r,g,b))

        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if e.type in [pygame.KEYDOWN]:
                if e.key==pygame.K_LEFT:dx=-5
                elif e.key==pygame.K_RIGHT:dx=+5
                elif e.key==pygame.K_UP:dy=-5
                elif e.key==pygame.K_DOWN:dy=+5
                elif e.key==pygame.K_SPACE:
                    if missileX == None:
                        missileX=shipX+shipSize[0]/2
                        missileY=shipY
        
            if e.type in [pygame.KEYUP]:
                if e.key==pygame.K_LEFT or e.key==pygame.K_RIGHT or e.key==pygame.K_UP or e.key==pygame.K_DOWN : dx,dy = 0,0

        if (0<shipX+dx and shipX+dx<=swidth-shipSize[0]) and (sheight/2<shipY+dy and shipY+dy <=sheight-shipSize[1]):
            shipX+=dx
            shipY+=dy
        paintEntity(ship,shipX,shipY)

        monsterX+=monsterSpeed
        if monsterX>swidth:
            monsterX=0
            monsterY=random.randrange(0,int(swidth*0.3))
            monster=pygame.image.load(random.choice(monsterImage))
            monsterSize=monster.get_rect().size
            monsterSpeed=random.randrange(1,5)
        paintEntity(monster,monsterX,monsterY)

        if missileX!=None:
            missileY-=10
            if missileY<0:
                missileX,missileY=None,None
        if missileX!=None:
            paintEntity(missile,missileX,missileY)

        pygame.display.update()
        print('~',end='')

r,g,b=[0]*3
swidth,sheight=500,700
monitor=None
ship,shipSize=None, 0

monsterImage=['C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster01.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster02.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster03.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster04.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster05.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster06.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster07.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster08.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster09.png','C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\monster10.png']
monster=None

missile=None

pygame.init()
monitor=pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship=pygame.image.load('C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\ship02.png')
shipSize=ship.get_rect().size

missile=pygame.image.load('C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.14\\game images\\missile.png')


playGame()