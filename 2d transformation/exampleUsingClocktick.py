import pygame
import sys
import time
pygame.init()
screen =pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
def translation(x1, y1, x2, y2,tx,ty):

    pygame.draw.line(screen,(255,255,255),(x1,y1),(x2,y2),width = 5)
    for i in range(1,10):
        nx1 = x1 + i*tx
        ny1 = y1 + ty
        nx2 = x2 + i*tx
        ny2 = y2 + ty
        pygame.draw.line(screen, (255,150,0),(nx1,ny1),(nx2,ny2), width = 5)
        pygame.display.flip()
        clock.tick(10)
    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill((0,0,0))
        translation(200,200,400,400,30,0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    