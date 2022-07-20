#Classes and Objects

class MyClass:
    x = 5
    
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)


print('#------------------Methods in Class------------------#')
class newClass:
    name = 'Bipul'

    def my_email(self):
        email = 'bipul@abc.com'
        print(email)

    def my_age(self):
        age = 33
        print(age)


c2 = newClass()     #object 

print(c2.name)
c2.my_email()
c2.my_age()

print('#------------------Arguments of Methods------------------#')

class my_class2:
    x = 2

    def new_name(self,name):
        n1 = name
        print(n1)

    def new_email(self,email):
        n2 = email
        print(n2)

c1 = my_class2()

print(c1.x)
c1.new_name('Bipul')
c1.new_email('Bipul@abc.com')

c1.new_name('John')

print(c1.n1)







    

