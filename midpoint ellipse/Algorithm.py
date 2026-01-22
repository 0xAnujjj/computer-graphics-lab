def ellipse():
# inputs
    xc = int(input("enter center x"))   
    yc = int(input("enter center y"))
    rM = int(input("enter major radius "))   
    rm = int(input("enter minor radius"))

# assign
    x = 0
    y = rm
    
# initial parameter for Region 1:
    p1 = rm**2 - (rM**2 * rm) + (rM)**2/4

    while((2 * rm**2 * x) <= (2 * rM**2 * y)):
        if(p1 < 0):
            x += 1
            p1 = p1 + 2 * rm**2 * x + rm**2
        
        else:
            x += 1
            y -= 1
            p1 = p1 + 2* rm**2 * x - 2* rM**2 * y + rm**2
        
        print(x,y)

# for region 2:
    p2 = rm**2 * (x + 1/2)**2 + rM**2 * (y - 1)**2 - rM**2 * rm**2

    while(y!= 0):
        if(p2 > 0):
            y = y-1
            p2 = p2 - 2* rM**2 * y + rm**2
        else:
            x = x+1
            y = y-1
            p2 = p2 - 2* rM**2 * y + 2* rm**2 * x + rM**2
        
        print(x,y)



ellipse()