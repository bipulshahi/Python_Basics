print('***************************Function*******************************')
def my_func(x1):
    z = x1
    return z + 5


p1 = my_func(4) 
p2 = my_func(5) 

print(p1)
print(p2)

#print(p1.z)
#print(p2.z)

print('***************************Class*******************************')

class calc:
    def my_calc(self , x1):
        self.z = x1
        return (self.z + 5)

c1 = calc()
c2 = calc()
c3 = calc()

print(c1.my_calc(3))
print(c2.my_calc(4))
print(c3.my_calc(5))

print(c1.z ,',' , c2.z , ',' , c3.z)

'''
t = c1.my_calc(3)
print(t)
print(t + p1)
'''

print('***************************Constructor*******************************')

class calc2:
    def __init__(self , x1):
        self.z = x1

ct1 = calc2(3)
ct2 = calc2(4)
ct3 = calc2(5)

print(ct1.z ,',' , ct2.z , ',' , ct3.z)


