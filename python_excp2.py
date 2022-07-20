#Try to write a file which is not writable

try:
    f = open('myfile.txt')
    try:
        f.write('Hello World')
    except:
        print('Something went wrong while writing the file')
    finally:
        f.close()
except:
    print('Something went wrong while accessing the file')

  
print('-------------------------Raise an Exception----------------------')

'''
x = -1
if x < 0:
    raise Exception("Sorry, number is less then 0")
'''

x = 'hello'
if not type(x) is int:
    raise Exception("Only Integers are Allowed")
