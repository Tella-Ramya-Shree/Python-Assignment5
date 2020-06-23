#Area of a Segment of a Circle Formula using math function
r=int(input('Radius:'))
from math import pi
x=float(input('Angle:'))
area=(pi*r**2)*(x/360)
print('Area of segment of a circle :',area)