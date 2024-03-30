#write a function in python to count the number of lines in a text file'story.txt' 
#which are starting with the letter a 
file=open("STORY.TXT",'r')
lines=file.readlines()
count=0
for w in lines:
    if w[0]=='A' or w[0]=='a':
        count+=1
        print("total lines is :",count)
        file.close()

