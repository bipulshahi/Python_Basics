#Constructor or Initialiser in a class

class my_class:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        my_class.count += 1

    def myfunc(self):
        print("Hello,",self.name,"Age is",self.age)

    def total_count(self):
        return my_class.count



c1 = my_class("Joe",22)
print(c1.total_count())

c2 = my_class("John",45)
print(c2.total_count())

c3 = my_class("Bipul",12)
print(c3.total_count())

c1.myfunc()
c2.myfunc()
c3.myfunc()

print('---------delete a element-------------')
del c1.age

#del c1 >> delete all the values associated with object c1

print(c2.age , c3.age)
print(c1.name,c2.name,c3.name)

print(c1.age)









