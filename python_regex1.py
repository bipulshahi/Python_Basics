#RegEx : - Regular Expressions

import re

text = "The rain in France"

#search: - search the string to see if it starts with The and ends with France
x = re.search("^The.*France$",text)
print(x)


#findall() - returns list of all matches
y1 = re.findall("in",text)
print(y1)

y2 = re.findall("Spain",text)
print(y2)


#Search for first whitespace character
x2 = re.search('\s',text)
print('The first white space character is located in position',x2.start())

#split
x3 = re.split("\s",text)
print(x3)

x4 = re.split("\s",text,1)
print(x4)

#sub()
x5 = re.sub('\s','_',text)
print(x5)

x6 = re.sub('\s','_',text,2)
print(x6)


x7 = re.search(r"\bFra",text)
print(x7)
print(x7.span())   #start and end location of match
print(x7.string)   #the passed string
print(x7.group())  #the part of string where there was a match





