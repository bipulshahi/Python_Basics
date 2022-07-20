#for loop-

'''
for i in range(0,10):
    print(i,'hello')
'''

#WAP for login where user name or password will be asked till the time it became correct

while True: 
    uname = input('Enter user name')
    if (uname == 'abcde'):
        upass = input('Enter Password')
        while (upass != '12345'):
            print('Incorrect Password,Try Again')
            upass = input('Enter Password')
        else:
            print('Login Success')
            break
    else:
        print('Incorrect User Name, Try Again')
    

#Modification :- Incorrect password attempt = 5

a = 1
while a == 1: 
    uname = input('Enter user name')
    if (uname == 'abcde'):
        a -= 1
        i = 5
        upass = input('Enter Password')
        while (upass != '12345'):
            if i > 1:
                i -= 1           
                print('Incorrect Password,Try Again')
                upass = input('Enter Password')
            else:
                print('No more Attempt')
                break
        else:
            print('Login Success')
            break
    else:
        print('Incorrect User Name, Try Again')






