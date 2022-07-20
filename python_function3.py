#Lambda function in python

#lambda arguments : expression

#Add 5 to the argument

def my_func(a):
    return (a + 5)

print(my_func(10))


print('--------------Lambda--------------------')

x = lambda a : a + 5
print(x(15))

#multiply argument a with b
x = lambda a,b : a * b
print(x(5,6))

#take 3 arguments and return the sum value...
x = lambda a,b,c : a + b + c
print(x(4,7,3))


#function that can take one argument and that arguments needs to be
#multiplied with an unknown number
def myfunc(x):
    return lambda y : y * x

z = myfunc(5)
print(z(11))

#WAF which can triples the number you put
def myfunc(x):
    return lambda y : y * x

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(9))
print(mytripler(5))


#program to filter out only even items from a given list
mylist = [1,3,4,5,6,2,11,12,13,15,16,18,19]

x = []
for val in mylist:
    if val % 2 == 0:
        x.append(val)
print(x)

y = [val for val in mylist if val % 2 == 0]
print(y)


z = list(filter(lambda x : (x%2 == 0), mylist))
print(z)

print('------Filter function Example------')
def fun(var):
    letters = ['a','i','e','o','u']
    if var in letters:
        return True
    else:
        return False


sequence = ['g','a','e','j','k','s','p','r']

#filter function
filtered = filter(fun ,sequence)
print(list(filtered))


print('------Map function Example------')

mylist = [1,3,4,5,6,2,11,12,13,15,16,18,19]

newlist = list(map(lambda x : x * 2 , mylist))
print(newlist)

print('**************************************')

def double_func(x):
    return x*2
nlist = list(map(double_func , mylist))
print(nlist)

print('**************************************')

nlist2 = [val * 2 for val in mylist]
print(nlist2)


