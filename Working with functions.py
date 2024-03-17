# Program to add two numbers through a function
def calcsum(x, y):
    s = x + y
    return s

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

result = calcsum(num1, num2)  # Call the function and store the result

print("Sum:", result)  # Print the result
