import pygame 
import sys
pygame.init()
W,H = 800,600
screen = pygame.display.set_mode((W,H))

White = (255, 255, 255)
Black = (0, 0, 0)

# print('Enter the first points:')
# x1 = int(input())
# y1 = int(input())
# print('Enter the second points:')
# x2 = int(input())
# y2 = int(input())

def draw_line_dda(x1,y1,x2,y2):

    # calculate
    dx = x2 - x1
    dy = y2 - y1

    step = max(abs(dx), abs(dy))

    # calculate:
    Xinc = dx/step
    Yinc = dy/step

    # assign:
    x = x1
    y = y1

    # repeat:
    for i in range(step):
        screen.set_at((round(x), round(y)), White)
        x += Xinc
        y += Yinc


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(Black)
        
        # Roof
        draw_line_dda(200, 150, 300, 50)
        draw_line_dda(300, 50, 400, 150)
        draw_line_dda(200, 150, 400, 150)

        # House body (rectangle)
        draw_line_dda(200, 150, 200, 300)
        draw_line_dda(400, 150, 400, 300)
        draw_line_dda(200, 300, 400, 300)

        # Door
        draw_line_dda(270, 220, 270, 300)
        draw_line_dda(330, 220, 330, 300)
        draw_line_dda(270, 220, 330, 220)
     
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
