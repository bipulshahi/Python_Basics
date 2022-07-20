#functions in Python

def my_function():
    print('hello world')

my_function()

print('-------------------------------------')

def new_func(name):
    print('Hello' , name)

new_func("Bipul")
new_func("John")
new_func("Merry")

print('-------------------------------------')
#create a function to print first name and last name together
def fullname(fname,lname):
    return (fname + " " + lname)

print('Hello' , fullname('Bipul','Kumar'))
print('Hello' , fullname('Donald','Trump'))

print('-------------------------------------')
#function with number of arguments are not known
def my_function(*kids):
    print("The youngest child is " + kids[len(kids)-1])
    print(len(kids))


my_function('Linus','Emil','Joe')

print('-------------------------------------')
#Keyword arguments
def my_func(c1,c2,c3):
    print('The youngest child is',c2)

my_func('Linus','Emil','Joe')

def my_func(c1,c2,c3):
    print('The youngest child is',c2)

my_func(c2 = 'Linus',c1 = 'Emil',c3 = 'Joe')

print('-------------------------------------')

#Number of keyword arguments are unknown
def myfunc(**kid):
    print('His last name is ' + kid["lname"])

myfunc(fname = "Tobias" , lname = "Refsnes")

print('-------------------------------------')
def my_function(country = "Norway"):
    print("He is from" , country)
    
my_function()
my_function("USA")
my_function("Srilanka")
my_function("France")


print('-------------------------------------')
#List as a parameter or argument

def my_function(fruits):
    for x in fruits:
        print(x)
my_function(["apple","oranges","mango"])


def my_function(*kids):
    for x in kids:
        print(x)
my_function('Linus','Emil','Joe')
