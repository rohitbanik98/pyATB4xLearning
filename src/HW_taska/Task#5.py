# - Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num_1 = float(input("Enter num_1 "))
num_2 = float(input("Enter num_2 "))

if(num_1 > num_2):
    print("num_1 is greater")
elif(num_1 == num_2):
    print("num_1 is equal to num_2")
else:
    print("num_2 is greater")


