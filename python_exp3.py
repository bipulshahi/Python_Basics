#NameError :- when variable is not existing
#IOError :- if the file can't be opened
#KeyboardInterrupt :- when an unrequired key is pressed by the user
#ValueError :- when built-in function receives a wrong argument
#EOFError :- if End-of-File is hit without reading any data
#Import Error :- if it is unable to import the module

def divide(x,y):
    try:
        z = x / y
        print(z)
    except ZeroDivisionError:
        print("Sorry! You are dividing by 0")

divide(3,0)
