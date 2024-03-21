#working with cvs files
import csv

# writing in cvs
#write a program to create a csv file to store student data(rollno,name,marks)obtain data from the user
#and write 5 records into the file

# file=open("student.csv",'w')
# writer=csv.writer(file)
# writer.writerow(['rollno','name','marks'])
# for i in range(5):
#     print("student record",(i+1))
#     rollno=int(input("enter rollno"))
#     name=input("enter your name")
#     marks=int(input("enter your marks"))
#     sturec=[rollno,name,marks]
#     writer.writerow(sturec)
# file.close()

#to add data in csv
# myfile=open("compresult.csv",'w')
# cswriter=csv.writer(myfile)
# compdat=[
#     ['name','points','rank'],
#     ['shradha',4500,23],
#     ['nishchay',4800,31],
#     ['ali',4500,25],
#     ['name',5100,14]]
# cswriter.writerow(compdat)
# myfile.close()

#to read csv file
file=open("compresult.csv",'r',newline='\r\n')
reader=csv.reader(file)
for rec in reader:
    print(rec)