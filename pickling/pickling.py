#learning how to write into binary file

#write a program to a binary file called emp.dat and write into it the employee details of some employees
#available in the form of dictionaries
# import pickle
# emp1={"empno":1201,"name":"anushre","age":25,}
# emp2={"empno":1202,"name":"zoya","age":30,}
# emp3={"empno":1203,"name":"simarjeet","age":27,}
# #opening the file
# f=open("emp.dat",'wb')
# #to write into the file
# pickle.dump(emp1,f)
# pickle.dump(emp2,f)
# pickle.dump(emp3,f)
# print("successfully writen 4 dictionaries")
# f.close()

# Write a program to get student data (roll no., name and marks) from user and write onto binary file
# The program should be able to get data from the user and write onto the file as long as the user wants

# import pickle
# stu={}
# file=open("stu.dat",'wb')
# ans='y'
# while ans=='y':
#     rno=int(input("enter roll no"))
#     name=input("enter name")
#     marks=int(input("marks"))
#     stu['rollno']=rno
#     stu['name']=name
#     stu['marks']=marks
#     pickle.dump(stu,file)
#     ans=input("want to enter more records?(y,n)")
# file.close()
#
# #to read the file
# emp={}
# myfile=open("stu.dat",'rb')
# try:
#     emp=pickle.load(myfile)
#     print(emp)
# except EOFError:
#     myfile.close()
#
# #write a program to open stu.dat and search for records with roll no 1 or 2
# #if found display the records
# stu={}
# found=False
# file=open("stu.dat",'rb')
# searchkey=[1,2]
# try:
#     while True:
#         stu=pickle.load(file)
#         if stu['rollno'] in searchkey:
#             print(stu)
#             found=True
# except EOFError:
#     if found==False:
#         print("not found")
#     else:
#         print("search successful")
#         file.close()
#
# #to find records with marks >81
# filee=open("stu.dat",'rb')
# stb={}
# Found=False
# try:
#     while True:
#         stb=pickle.load(filee)
#         if stb['marks']>81:
#             print(stb)
#             found=True
# except EOFError:
#     if found==False:
#         print("not found")
#     else:
#         print("search successful")
#         filee.close()
#
#to update a file
# import pickle
# found=False
# stu={}
# g=open("stu.dat",'rb+')
# try:
#     while True:
#         repos=g.tell()
#         stu=pickle.load(g)
#         if stu['marks']>81:
#             stu['marks']+=2
#             g.seek(repos)
#             pickle.dump(stu,g)
#             found=True
# except EOFError:
#     if found==False:
#         print("not found")
#     else:
#         print("successful")
#         g.close()

#to display new information
# import pickle
# stu={}
# file=open("stu.dat",'rb')
# try:
#     while True:
#         stu=pickle.load(file)
#         print(stu)
# except EOFError:
#     file.close()

# a program to modify the name of rolno 1 as gurnam
import pickle

stu = {}
found = False

# Open the file in read-write mode
with open("stu.dat", 'rb+') as file:
    try:
        while True:
            # Get the current file position
            rpos = file.tell()
            # Load student record
            stu = pickle.load(file)
            # Check if the roll number is 1
            if stu['rollno'] == 1:
                # Update the name to 'gurnam'
                stu['name'] = 'gurnam'
                # Move file pointer to the previous record position
                file.seek(rpos)
                # Write the updated record back to the file
                pickle.dump(stu, file)
                found = True
    except EOFError:
        pass  # End of file reached
    # Check if any records were found and updated
    if found:
        print("Successful")
    else:
        print("Not found")
