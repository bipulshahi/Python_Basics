#Math

x = min(4,14,3)
y = max(5,25,20)
z = abs(-7.25)
a = pow(4,3)
print(x , y, z ,a)


#math module
import math

x1 = math.sqrt(64)
print(x1)

x2 = math.ceil(1.4)
x3 = math.floor(1.7)

print(x2)
print(x3)

x4 = math.pi
print(x4)

x5 = math.factorial(5)
print(x5)

#gcd :- greatest common divisior
x6 = 15
x7 = 5
print(math.gcd(x6,x7))


a1 = 4
a2 = -3
a3 = 0
print(math.exp(a1))
print(math.exp(a2))
print(math.exp(a3))

#log() : log value of a with base b
#log2(a) : - log value of a with base 2
#log10(a) : log value of a with base 10

print(math.log(2,3))
print(math.log2(16))
print(math.log10(10000))

#sin,cos,tan

print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

#degrees() - from radians to degree
#radians() - from degree to radians

a4 = math.pi/6
a5 = 30

print(math.degrees(a4))
print(math.radians(a5))

#check if a value is infinity or not

print(math.isinf(math.pi))
print(math.isinf(float('inf')))

#check if a value is null or not

print(math.isnan(math.pi))
print(math.isnan(float('nan')))







