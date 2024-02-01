print("CALCULATOR")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("OPTIONS\n 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division")
n=int(input("Enter your option:"))
if n==1:
    c=a+b
    print("Result:",c)
elif n==2:
    c=a-b
    print("Result:",c)
elif n==3:
    c=a*b
    print("Result:",c)
elif n==4:
    c=a/b
    print("Result:",c)
else:
    print("Invalid Choice")

