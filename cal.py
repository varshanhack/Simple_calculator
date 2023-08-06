#Simple calculator
import sys,subprocess
while True:
    print("Simple Calculator\n")
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n")    
    ch=int(input("Enter the choice number ==> "))
    print("")
    a=int(input("Enter first number ==> "))
    b=int(input("Enter second number ==> "))
    print("")
    if ch==1:
        print("The Addition is",a+b)
    elif ch==2:
        print("The Subtraction is",a-b)
    elif ch==3:
        print("The Multiplication is",a*b)
    elif ch==4:
        print("The Division is",a/b)
    elif ch==5:
        print("The Remainder is",a%b)
    else:
        print("Invalid input...")
    print("")
    input("Press enter to continue...")
    subprocess.run("cls",shell=True)
