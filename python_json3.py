#Writing and reading a json file

import json

data = {'employee':
        [{'name' : 'John Doe',
          'department' : 'Software Engineer',
          'place' : 'remote'},

         {'name' : 'Jane Doe',
          'department' : 'Software Engineer',
          'place' : 'remote'},

         {'name' : 'Don Joe',
          'department' : 'Software Engineer',
          'place' : 'remote'}]
        }

json_string = json.dumps(data , indent=4)
print(json_string)

#using a json string
with open('json_data.json' , 'w') as outfile:
    outfile.write(json_string)


#Directly from Dictionary
outfile = open('new_json_data.json' , 'w')
json.dump(data , outfile)
outfile.close()

print('------------------------------------Read Json File------------------------')

import json
json_file = open('json_data.json')
dfx = json.load(json_file)
json_file.close()
print(dfx , type(dfx))




    
