'''
FILE HANDLING
It allows us to store data in less complex strucutre
Types
Text file -> .doc , .txt , .py , .html
Binary File -> .png , .jpg , .pdf
text file: 
r -> read mode
w -> write mode
a -> append mode
binary file:
rb -> read mode
wb -> write mode
'''

# writing in the file


# appending 
# after writing we can append the data
'''
file = open("./test.txt",'w')
file.write("Hello, we are writing")
file.close()

file = open("./test.txt",'a')
file.write("Python file handling")
file.close()

with open("./test.txt","r") as f1:
    print(f1.read())
'''
#copying the whole file

