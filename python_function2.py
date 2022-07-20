def my_func(x):
    return(x + 2)

print(my_func(3) * 2)
print(my_func(5) * 3)

print('------------------------------------------------------------------')

#Recursion: - define a function which can call itself

def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k - 1)
        return result
    else:
        result = 0
    return result

print(tri_recursion(6))

#WAF to calculate factorial

def tri_recursion(k):
    if (k>0):
        result = k * tri_recursion(k - 1)
        return result
    else:
        result = 1
    return result

print(tri_recursion(6))

print('------------------------------------------------------------------')


#Create a recusive function to create countdown
def countdown(n):
    print(n)
    if n == 0:
        return 0
    else:
        countdown(n-1)
    

countdown(9)

print('------------------------------------------------------------------')

def countdown(i):
    while i>=0:
        print(i)
        i-=1


countdown(7)

print('------------------------------------------------------------------')

def countdown(n):
    print(n)
    return 0 if n==0 else countdown(n-1)    

print(countdown(9))

print('------------------------------------------------------------------')

def tri_factorial(n):
    return 1 if n <= 1 else n * tri_factorial(n-1)

print('One liner',tri_recursion(6))

print('------------------------------------------------------------------')

#Calculate factorial without using recursion
def factorial(n):
    return_val = 1
    for i in range(2 , n+1):
        return_val *= i
    return return_val

print(factorial(5))






