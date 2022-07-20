#writing a file

f = open("myfile2.txt","wt")
print(f.write("Hello Guys, How are You..."))
f.close()

f = open("myfile2.txt","at")
print(f.write("\n Are you going to watch a movie"))
f.close()

f = open("myfile2.txt","rt")
print(f.read())
print(f.close())

#f = open("myfile4.txt" , 'x')


#Delete a file
#import os
#os.remove("myfile3.txt")
