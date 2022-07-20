class data_chain:
    def __init__(self):
        self.collection = []
        self.index = 0
        
    def data_block(self,name,email,age,cty):
        self.index += 1
        details = {'Index': self.index,
                   'name': name,
                   'email': email,
                   'age': age,
                   'Country': cty}
        self.collection.append(details)
        return details

    def data_collection(self):
        response = {'data' : self.collection,
                    'data_length' : len(self.collection)}
        return response



c1 = data_chain()
c1.data_block('Joe','Joe@abc.com',23,'France')
c1.data_block('Merry','Merry@abc.com',56,'Germany')
c1.data_block('Bipul','Bipul@abc.com',66,'India')

print(c1.data_collection())

print(c1.data_collection()['data'][0])
print(c1.data_collection()['data_length'])

