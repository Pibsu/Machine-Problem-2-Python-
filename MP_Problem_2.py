#MP2-Python
import math as m
import numpy as np
x1,y1 = [float(x) for x in input('Please input 1st point: ').split(',')]
x2,y2 = [float(x) for x in input('Please input 2nd point: ').split(',')]
x3,y3 = [float(x) for x in input('Please input 3rd point: ').split(',')]
print('The points are: \n',
      '(',x1,',',y1,')\n', 
      '(',x2,',',y2,')\n',
      '(',x3,',',y3,')\n')
sqx1y1 = x1**2 + y1**2
sqx2y2 = x2**2 + y2**2
sqx3y3 = x3**2 + y3**2
Amat = np.array([[x1,y1,1],[x2,y2,1],[x3,y3,1]])
Dmat = -1*(np.array([[sqx1y1,y1,1],[sqx2y2,y2,1],[sqx3y3,y3,1]]))
Emat = np.array([[sqx1y1,x1,1],[sqx2y2,x2,1],[sqx3y3,x3,1]])
Fmat = -1*(np.array([[sqx1y1,x1,y1],[sqx2y2,x2,y2],[sqx3y3,x3,y3]]))
A = round((np.linalg.det(Amat)),3).astype(int,copy=True)
D = round((np.linalg.det(Dmat)),3).astype(int,copy=True)
E = round((np.linalg.det(Emat)),3).astype(int,copy=True)
F = round((np.linalg.det(Fmat)),3).astype(int,copy=True)
d = m.gcd(m.gcd(D,A),m.gcd(E,F))
Alt = A // d
Dlt = D // d
Elt = E // d
Flt = F // d
v = np.array([(Dlt,Elt,Flt)])
h = int(round(-(Dlt/2*Alt)))
k = int(round(-(Elt/2*Alt)))
r2 = (x1 - h)**2 + (y1 - k)**2 
r = m.sqrt(r2)
print('General Equation: x^2 + y^2 + ',Dlt,'x +',Elt,'y +',Flt)
print('Vector DEF: ',v)
print('Center of Circle: (',h,',',k,')')
print('Radius of Circle: ',r)
