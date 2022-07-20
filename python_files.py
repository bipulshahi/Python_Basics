#file Handling

#open() - used to open a file
#"r" - Read - Opens a file for reading, error if file does not exist.
#"a" - Append - Opens a file for appending , creates a file if it does not exist.
#"w" - Write - Opens a file for writing , creates a file if it does not exist.
#"x" - Cteate - Create the specified file , returns an error if the file exist

#"t" - Text - Default Mode . Handle the file in Text Mode
#"b" - Binary - Binary Mode . Handle the file in Binary Mode

f = open("myfile.txt","rt")   #read file in text mode
print(f.read())
f.close()

print('----------------------------------')

f = open("myfile.txt","rt")   #read file in text mode
print(f.read(10))
f.close()

print('----------------------------------')

f = open("myfile.txt","rt")   #read file in text mode
print(f.readline())             #returns one line at a time
print(f.readline())
f.close()

print('----------------------------------')

#Loop through the file line by line
f = open("myfile.txt","rt")
for x in f:
    print(x)
