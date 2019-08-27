def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
print("Select Operation")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choice=input("ENTER CHOICE (1/2/3/4):")
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
if choice=="1":
    print(num1,"+",num2,"=", add(num1,num2))
elif choice=="2":
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice=="3":
    print(num1,"X",num2,"=", multiply(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=", division(num1,num2))
else:
    print("Invalid Input")
    
