from sys import stdin,stdout
from math import gcd,ceil,sqrt,factorial,log
from decimal import Decimal as dec
input,print = stdin.readline,stdout.write

x,y,z = list(map(dec,input().split()))
ans = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y', 'y^x^z', 'y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
pos = []
pos.append([dec(log(x))*pow(y,z),0])
pos.append([dec(log(x))*pow(z,y),-1])
pos.append([dec(log(x))*y*z,-2])
pos.append([dec(log(x))*y*z,-3])
pos.append([dec(log(y))*pow(x,z),-4])
pos.append([dec(log(y))*pow(z,x),-5])
pos.append([dec(log(y))*x*z,-6])
pos.append([dec(log(y))*x*z,-7])
pos.append([dec(log(z))*pow(x,y),-8])
pos.append([dec(log(z))*pow(y,x),-9])
pos.append([dec(log(z))*y*x,-10])
pos.append([dec(log(z))*y*x,-11])
pos.sort(reverse = True)
print(f"{ans[-pos[0][1]]}\n")
