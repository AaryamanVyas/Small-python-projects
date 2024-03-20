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


#basic program on how to write into text files

#write a program to get roll numbers, names and marks of the students of a class(get from user)
# and store these details in a dile called "marks".txt
count=int(input("enter how many students inside the class"))
fileout=open("marks.txt",'w')
for i in range(count):
    print("enter details for student",(i+1),"below:")
    rollno=int(input("rolno:"))
    name=input("name:")
    marks=float(input("marks:"))
    rec = f"{rollno},{name},{marks}\n"
    fileout.write(rec)
fileout.close()

#write a program to read a text file line by line and display each word seperated by a "#"
myfile=open("marks.txt",'r')
while str:
    str=myfile.readline()
    print(str)
myfile.close()
#
# #write a program to read a text file and display the count of vovels ans consonants in the file
file = open("marks.txt", 'r')
content = file.read()  # Read the entire content of the file
file.close()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in content:
    if char.isalpha():  # Check if the character is an alphabet
        if char.lower() in vowels:  # Convert to lowercase for comparison
            vowel_count += 1
        else:
            consonant_count += 1

print("The number of vowels in the file:", vowel_count)
print("The number of consonants in the file:", consonant_count)
file.close()