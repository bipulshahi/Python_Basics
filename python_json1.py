#Json

print('---------------------Json to Dictionary------------------------')
import json

x = '{"name" : "John" , "age" : 30 , "city" : "NYC"}'
print(x)
print(type(x))

#print(x['age'])

#parse x
y = json.loads(x)
print(y)
print(type(y))

print(y['age'])

print('---------------------Dictionary to Json------------------------')
a = {"name" : "John" , "age" : 30 , "city" : "NYC"}
print(a)

b = json.dumps(a)
print(b)
