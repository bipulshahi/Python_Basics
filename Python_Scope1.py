#Scope of a variable

print('-------------------------------Global Variable-----------------------------')
x = 30

def myfunc():
    print(x)

myfunc()
print(x)


print('-------------------------------Local Variable-----------------------------')

def l_func():
    y = 56
    print(y)

l_func()
#print(y)


def func1():
    z = 400
    def func2():
        print(z)
    func2()
    
func1()

print('-------------------------------Local + Global Variable-----------------------------')

k = 300
def newfunc():
    k = 400
    print(k)

newfunc()
print(k)

print('-------------------------------Global Keyword-----------------------------')

def n_func():        #create a new global variable p within a function
    global p
    p = 200

n_func()
print(p)



x = 55
def n_func():       #update the value of global variable x from a function
    global x
    x = 200

n_func()
print(x)

