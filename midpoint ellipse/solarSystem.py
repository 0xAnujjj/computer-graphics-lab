import pygame
import sys
import random
pygame.init()
W,H = 1000,1000
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)

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
        x = x + 1;
        if(p<0):
            y = y
            p = p + 2*x + 1
        else:
            y = y - 1
            p = p + 2*x - 2*y + 1

def ellipse(xc, yc, rM, rm):
# inputs given directly in args...

# assign
    x = 0
    y = rm
    
# initial parameter for Region 1:
    p1 = rm**2 - (rM**2 * rm) + (rM)**2/4

    while((2 * rm**2 * x) <= (2 * rM**2 * y)):
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        if(p1 < 0):
            x += 1
            p1 = p1 + 2 * rm**2 * x + rm**2
        
        else:
            x += 1
            y -= 1
            p1 = p1 + 2* rm**2 * x - 2* rM**2 * y + rm**2


# for region 2:
    p2 = rm**2 * (x + 1/2)**2 + rM**2 * (y - 1)**2 - rM**2 * rm**2

    while(y!= 0):
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        if(p2 > 0):
            y = y-1
            p2 = p2 - 2* rM**2 * y + rm**2
        else:
            x = x+1
            y = y-1
            p2 = p2 - 2* rM**2 * y + 2* rm**2 * x + rM**2
        
        # print(x,y)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill(BLACK)

        ellipse(500,500,80,30)
        ellipse(500,500,130,90)
        ellipse(500,500,180,130)
        ellipse(500,500,230,170)
        ellipse(500,500,280, 220)
        ellipse(500,500,330,270)
        ellipse(500,500,380,320)
        ellipse(500,500,430,370)

        # circle(500,500, 25) #sun
        circle(500 + 80, 500, 5)  #mercury
        circle(500 + 130, 500, 10) #venus
        circle(500 + 180, 500, 12) #earth
        circle(500 , 500 + 170, 13) #mars
        circle(500 + 280, 500, 15) #jupyter
        circle(500 + 330, 500, 18) #saturn
        circle(500, 500 + 320, 20) #uranus
        circle(500 + 430, 500, 23) #neptune

        pygame.display.flip()

if __name__ == "__main__":
    main()