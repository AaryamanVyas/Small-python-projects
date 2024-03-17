# Program to add two numbers through a function
def calcsum(x, y):
    s = x + y
    return s

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

result = calcsum(num1, num2)  # Call the function and store the result

print("Sum:", result)  # Print the result

#write a function Lshift(arr,n)in python, which accepts a list arr of numbers 
#and n is the numeric value by which all the elements of the list are shifted to left 

def Lshift(Arr,n):
    L=len(Arr)
    for x in range(0,n):
        y=Arr[0]
        for i in range(L-1):
            Arr[i]=Arr[i+1]
        Arr[L-1]=y
        return Arr
Arr=[10,20,30,40,12,11]
n=2
result=Lshift(Arr,n)
print(result)
