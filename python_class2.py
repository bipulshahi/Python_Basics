class my_class2:
    x = 22

    def new_name(self,name,age):
        self.n1 = name
        self.a1 = age
        print('Name:',self.n1 ,
              'Age:' ,self.a1 ,
              'Global Variable:' , my_class2.x)

    def new_email(self,email):
        self.n2 = email
        print('Name:',self.n1,
              'Email:',self.n2)

c1 = my_class2()
c2 = my_class2()

print(c1.x)
c1.new_name('Bipul',32)
c1.new_email('Bipul@abc.com')

print(c1.n1)
print(c1.a1)
print(c1.n2)

c1.new_name('John',33)
c2.new_name('Joe',24)

print('for c1 object:',c1.n1)
print('for c1 object:',c1.a1)
print('for c1 object:',c1.n2)


print('for c2 object:',c2.x)
print('for c2 object',c2.n1)
print('for c2 object',c2.a1)
