import pygame
import sys
pygame.init()
screen =pygame.display.set_mode((800,600))
def scaling(x1, y1, x2, y2, sx, sy):

    pygame.draw.line(screen,(255,255,255),(x1,y1),(x2,y2),width = 5)

#scaling: x' = x * Sx
    x22 = x2*sx
    y22 =y2*sy

    pygame.draw.line(screen, (255,255,150),(x2,y2),(x22,y22), width = 5)
    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill((0,0,0))
        scaling(100,100,200,200, 1.5, 2) #scaling with a bend
        pygame.display.flip()

if __name__ == "__main__":
    main()
    

