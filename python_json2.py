#Python Objects that can be converted into json

#dict,list,tuple,string,int,float,True,False,None

import json

print(json.dumps({"name":"json" , "age":33},
                 indent=4 ,
                 separators=(",, " , " > "),
                 sort_keys = True))
print(json.dumps(["apple","oranges"]))
print(json.dumps(("apple","oranges")))
print(json.dumps("hello"))
print(json.dumps(33))
print(json.dumps(31.67))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
