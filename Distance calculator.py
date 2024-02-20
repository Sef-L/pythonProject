import math

def distance(x1,y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

point1 = input("Enter the coordinates of the first point in x,y format: ")
point2 = input("Enter the coordinates of the next point in x,y format: ")

point1 = point1.split(',')
point2 = point2.split(',')

if len(point2) != 2 or len(point1) != 2:
    raise ValueError('R u stupid or sumthing?')
x1, y1 = point1
x2, y2 = point2
print('\n',distance(x1,y1,x2,y2))