#datetime

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))


#create a datetime

y = datetime.datetime(2020,5,20)
print(y)

z = datetime.datetime(2020,5,21)
print(z.strftime('%A') , z.strftime('%w'))
print(z.strftime('%B'))
print(z.strftime('%C'))
