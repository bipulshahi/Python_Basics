#string formatting

price = 66
txt1 = "The price is {} dollars"
print(txt1.format(price))

#to use a value upto 2 decimal palce
price = 34.56321
txt2 = "The price is {:.2f} dollars"
print(txt2.format(price))


#Multiple values :- multiple placeholders
quantity = 3
itemno = 456
price = 46

myorder1 = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder1.format(quantity,itemno,price))

myorder2 = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder2.format(quantity,itemno,price))


age = 44
name = "John"

txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age,name))


#named indexes
myorder = "I have a {carname}, it is a {model}"
print(myorder.format(model="Mustang",carname="Ford"))
