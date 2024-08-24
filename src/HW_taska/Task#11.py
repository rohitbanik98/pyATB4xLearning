# - Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13


num = int(input("Enter number"))
a = 1
b = 0
for i in range(1,num):
    c = a + b
    print(c)
    b = a
    a = c





