import pygame
import sys
pygame.init()

W,H = 800,600
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)

def DDAline(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1

    if(abs(dx)>abs(dy)):
        step = abs(dx)
    else:
        step = abs(dx)
    xinc = dx/step
    yinc = dy/step
    x = x1
    y = y1
    for i in range(step):
        x = x + xinc
        y = y + yinc
        screen.set_at((round(x),round(y)),WHITE)

def circle(xc, yc, r):
    x = 0
    y = r
    p = 1-r
    while(x<y):
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + y, yc + x), WHITE)
        screen.set_at((xc - y, yc + x), WHITE)
        screen.set_at((xc - y, yc - x), WHITE)
        screen.set_at((xc + y, yc - x), WHITE)
        x = x + 1
        if(p<0):
            y = y
            p = p + 2*x + 1
        else:
            y = y - 1
            p = p + 2*x - 2*y + 1

def circle_mouth(xc,yc,r):
    x = 0
    y = r
    p = 1-r
    while(x<y):
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc + y, yc + x), WHITE)
        screen.set_at((xc - y, yc + x), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)

        x = x + 1
        if(p<0):
            y = y
            p = p + 2*x + 1
        else:
            y = y - 1
            p = p + 2*x - 2*y + 1

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        circle(100,100,50)
        circle(75,90,10)
        circle(125,90,10)
        circle_mouth(100,120,20)
        DDAline(100,150,100,300)
        DDAline(100,170,30,230)
        DDAline(100,170,170,230)
        DDAline(100,300,170,360)
        DDAline(100,300,30,360)

        pygame.display.flip()

if __name__ == "__main__":
    main()