#Break and continue in for loop
fruits = ["apple" , "mango" , "cherry" , "banana" ,"Pineapple"]

for x in fruits:
    print(x)
    if x == "cherry":
        break
print('-------------------------------------')

for x in fruits:
    if x == "cherry":
        break
    print(x)   
print('-------------------------------------')

for x in fruits:
    if x == "cherry":
        continue
    print(x)  
print('-------------------------------------')

for i in range(0,20,2):
    print(i)

print('-------------------------------------')
for i in range(20,0,-2):
    print(i)

print('-------------------------------------')
for x in range(6):
    print(x)
else:
    print("Finally finished")
    
print('-------------------------------------')
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished")

#Nested for loop
adj = ["red" , "big" , "tasty"]
fruits = ["apple","mango","oranges"]
for x in adj:
    for y in fruits:
        print(x,y)



