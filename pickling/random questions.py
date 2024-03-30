# #write a function in python to count the number of lines in a text file'story.txt' 
# #which are starting with the letter a 
# file=open("STORY.TXT",'r')
# lines=file.readlines()
# count=0
# for w in lines:
#     if w[0]=='A' or w[0]=='a':
#         count+=1
# print("total lines is :",count)
# file.close()

# #write a medthod/function DISPLAYWORDS() in python to read lines from story.txt
# #and display those words which are less than 4 characters
# def DISPLAYWORDS():
#     file=open("STORY.TXT",'r')
#     line=file.read()
#     words=line.split()
#     for word in words:
#         if len(word)<4:
#             print(word)
#     file.close()
# DISPLAYWORDS()

# testing by adding some text in story.txt
# file=open("STORY.TXT",'w')
# text='''hello this is my text 
# a new file is created 
# awesome is more than 4'''
# file.write(text)
# file.close()

#to find if line starts with p
# def countp():
#     file=open('STORY.TXT','r')
#     line=file.readlines()
#     for word in line:
#         if word[0]=='P' or word[0]=='p':
#             print(word)
#     file.close()
# countp()

#given text file car.txt conatining the following information of cars : carno,carname,milage.
#write a python function to display details of all those cars whoes milage is from 100 to 150
# file=open("car.txt",'r')
# text=file.readlines()
# file.close()
# for line in text:
#     x=line.split()
#     milage=(int)(x[2])
#     if milage>100 and milage<150:
#         print(line)

#write a method in python to write multiple lines of text contents into a file, "myfile.txt" line.
# file=open('myfile.txt','w')
# while True:
#     text=input("enter line")
#     file.write(text)
#     choice=input("enter more lines?")
#     if choice =='N':
#         break


# def countfirstdigit():
#     count=0
#     file=open("diary.txt",'r')
#     text=file.readlines()
#     for word in text:
#         if word[0].isdigit():
#             count+=1

# file = open("STORY.TXT",'r')
# w=int(input("enter number"))
# file.seek(w)
# text=file.read()
# print(text)
# file.close()

# def ISTOUPCOUNT():
#     count=0
#     file=open("STORY.TXT")
#     text=file.read()
#     words=text.split()
#     for word in words:
#         if word=='is' or word=='to' or word=='up':
#             count+=1
#     print(count)
#     file.close()
# ISTOUPCOUNT()

import pickle
def createfile():
    file=open("book.dat",'w')
    bookno=int(input("book number"))
    bookname=input("enter name")
    author=input("enter author")
    price=float(input("price"))
    rec=[bookno,bookname,author,price]
    pickle.dump(rec,file)
    file.close()
def countrec():
    author=input("enter author name")
    file=open("book.dat",'rb')
    num=0
    try:
        while True:
            rec=pickle.load(file)
            if author==rec[2]:
                num=num+1
    except:
        file.close()
        return num
createfile()