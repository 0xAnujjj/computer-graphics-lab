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

def draw_star(x, y):
    # Draw a small star as a plus sign
    screen.set_at((x, y), WHITE)
    screen.set_at((x+1, y), WHITE)
    screen.set_at((x-1, y), WHITE)
    screen.set_at((x, y+1), WHITE)
    screen.set_at((x, y-1), WHITE)

def draw_comet(x, y, tail_length=20):
    # Draw comet head
    circle(x, y, 3)
    # Draw tail as a line
    for i in range(1, tail_length):
        screen.set_at((x - i, y), WHITE)

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
        # Add some stars
        draw_star(100, 100)
        draw_star(200, 150)
        draw_star(300, 200)
        draw_star(400, 250)
        draw_star(600, 300)
        draw_star(700, 350)
        draw_star(800, 400)
        draw_star(900, 450)
        
        # Add comets
        draw_comet(200, 200)
        draw_comet(700, 300)
        
        ellipse(500,500,80,30)
        ellipse(500,500,130,90)
        ellipse(500,500,180,130)
        ellipse(500,500,230,170)
        ellipse(500,500,280, 220)
        ellipse(500,500,330,270)
        ellipse(500,500,380,320)
        ellipse(500,500,430,370)
        # circle(500,500, 25) #sun
        pygame.draw.circle(screen, (128,128,128), (500 + 80, 500), 5)  #mercury - gray
        pygame.draw.circle(screen, (255,220,0), (500 + 130, 500), 10)  #venus - yellow
        pygame.draw.circle(screen, (0,0,255), (500 + 180, 500), 12)  #earth - blue
        pygame.draw.circle(screen, (255,0,0), (500, 500 + 170), 13)  #mars - red
        pygame.draw.circle(screen, (255,165,0), (500 + 280, 500), 15)  #jupiter - orange
        pygame.draw.circle(screen, (255,255,0), (500 + 330, 500), 18)  #saturn - yellow
        pygame.draw.circle(screen, (0,255,255), (500, 500 + 320), 20)  #uranus - cyan
        pygame.draw.circle(screen, (0,0,139), (500 + 430, 500), 23)  #neptune - dark blue

        pygame.draw.circle(screen, (255,255,0), (500,500), 25) #sun - yellow
        
        pygame.display.flip()

if __name__ == "__main__":
    main()