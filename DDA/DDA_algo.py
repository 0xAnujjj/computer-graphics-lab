'''
DDA LINE ALGORITHM
'''
# Input end points x1,y1 and y1,y2
print('Enter the first points:')
x1 = int(input())
y1 = int(input())
print('Enter the second points:')
x2 = int(input())
y2 = int(input())

 # calculate
dx = abs(x2 - x1)
dy = abs(y2 - y1)

if (dx > dy):
    step = dx
else:
    step = dy

 # calculate:
Xinc = dx/step
Yinc = dy/step

 # assign:
x = x1
y = y1

 # repeat:
for i in range(step):
    x += Xinc
    y += Yinc
    print(x, y)