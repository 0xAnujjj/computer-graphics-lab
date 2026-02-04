import pygame
import sys
import math

pygame.init()
screen =pygame.display.set_mode((800,600))
def rotation(x1, y1, x2, y2, theta):

    pygame.draw.line(screen,(255,255,255),(x1,y1),(x2,y2),width = 5)

#rotation: x' = x cos(theta) - y sin(theta) & y' = x sin(theta) + y cos(theta)

    angle_rad = math.radians(theta)
    x22 = x2*math.cos(angle_rad) - y2* math.sin(angle_rad)
    y22 = x2* math.sin(angle_rad) + y2* math.cos(angle_rad)

    pygame.draw.line(screen, (255,255,150),(x2,y2),(x22,y22), width = 5)
    print(x22, y22)    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.fill((0,0,0))
        rotation(100,100,200,200, 20) #scaling with a bend
        pygame.display.flip()

if __name__ == "__main__":
    main()
    