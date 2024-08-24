# create a program for sum of three numbers

num1 = int(input("Enter num1\n"))
num2 = int(input("Enter num2\n"))
num3 = int(input("Enter num3\n"))

def sum_of_three(n1,n2,n3):
    return n1 + n2 + n3

result = sum_of_three(num1,num2,num3)
print(result)

result = sum_of_three(1,2,3)
print(result)