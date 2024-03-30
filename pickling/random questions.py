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
