#Exception Handling


#Try - test a block of code for errors
#except - to handle the error
#else - to execute a code when there is no error
#finally - lets tou execute the code regardless of the result of try and except blocks

try:
    print(x)
except NameError:
    print('Variable x is not defined')
except:
    print('Something else wemt wrong')
else:
    print('Nothing went wrong')
finally:
    print('The try-catch is finished')

print('--------------------------------------------------------')

try:
    print('Hello')
except:
    print('Something Went Wrong')
else:
    print('Nothing went wrong')
finally:
    print('The try-catch is finished')
