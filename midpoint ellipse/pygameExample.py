import pygame
import sys
pygame.init()
W,H = 800,600
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)

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
        
        # print(x,y)

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
        ellipse(150,100,100,50)

        pygame.display.flip()

if __name__ == "__main__":
    main()