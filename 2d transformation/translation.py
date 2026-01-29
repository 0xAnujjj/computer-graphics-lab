import pygame
import sys
pygame.init()
screen =pygame.display.set_mode((800,600))
def translation(x1, y1, x2, y2, tx, ty):

    pygame.draw.line(screen,(255,255,255),(x1,y1),(x2,y2),width = 5)

    x1 += tx
    y1 += ty
    x2 += tx
    y2 += ty

    pygame.draw.line(screen, (255,255,0),(x1,y1),(x2,y2), width = 5)
    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill((0,0,0))
        translation(200,200,400,400, 190, 190)
        pygame.display.flip()

if __name__ == "__main__":
    main()
    

