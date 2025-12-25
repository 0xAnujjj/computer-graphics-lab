import pygame
import sys
pygame.init()
W,H=800,600
screen = pygame.display.set_mode((W,H))
WHITE=(255,255,255)
BLACK=(0,0,0)

def draw_line_data(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1) 
    if x2>x1:
        lx = 1
    else:
        lx = -1

    if y2>y1:
        ly = 1
    else:
        ly = -1

    x = x1
    y = y1

    if dx > dy:
        p = 2*dy-dx
        for i in range(dx + 1):
            screen.set_at((round(x),round(y)),WHITE)
            if p < 0:
                x = x+lx
                p = p+2*dy
            else:
                x = x+lx
                y = y+ly
                p = p+2*dy-2*dx
    else:
        p = 2*dx-dy
        for i in range(dy + 1):
            screen.set_at((round(x),round(y)),WHITE)
            if p < 0:
                y = y+ly
                p = p + 2*dx
            else:
                x = x + lx
                y = y + ly
                p = p + 2*dx - 2*dy

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
 # Two vertical lines
        draw_line_data(250, 150, 250, 450)
        draw_line_data(350, 150, 350, 450)

        # Two horizontal lines
        draw_line_data(180, 250, 420, 250)
        draw_line_data(180, 350, 420, 350)
        pygame.display.flip()

if __name__=="__main__":
    main()
