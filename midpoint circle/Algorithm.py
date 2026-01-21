def circle():
    xc = int(input("Enter the x coordinate of center:"))
    yc = int(input("Enter the y coordinate of center"))
    r = int(input("Enter the radius"))
    x = 0
    y = r
    p = 1-r
    while(x<y):
        print(x,y)
        x = x + 1;
        if(p<0):
            y = y
            p = p + 2*x + 1
        else:
            y = y - 1
            p = p + 2*x - 2*y + 1

circle()