print('Enter the first points:')
x1 = int(input())
y1 = int(input())
print('Enter the second points:')
x2 = int(input())
y2 = int(input())

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
            print(x, y)
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
            print(x, y)
            if p < 0:
                y = y+ly
                p = p + 2*dx
            else:
                x = x + lx
                y = y + ly
                p = p + 2*dx - 2*dy

draw_line_data(x1,y1,x2,y2)