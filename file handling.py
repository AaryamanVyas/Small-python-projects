#basic program on how to read a file

#program to display the size of a file in bytes
myfile=open(r"C:\Users\aarya\OneDrive\Documents\words.txt",'r')
#here we open an file through python and the 'r' is required for reading
str=myfile.read()
#this reads the file
size=len(str)
#this determines the length of the file
print("size of the given file is:")
print(size,"bytes")
#this will tell the size in bytes
myfile.close()

#to write a program to display number of lines in a file
myfile=open(r"C:\Users\aarya\OneDrive\Documents\words.txt",'r')
s=myfile.readlines()
linecount= len(s)
print("number of lines are :",linecount)
myfile.close()



#