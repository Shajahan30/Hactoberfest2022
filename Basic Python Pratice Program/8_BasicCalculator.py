def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def divide(a,b):
    return a/b;

n1=float(input("enter 1st number: "))
n2=float(input("enter 2nd number: "))
def operation(a,b):
    
    op=input("enter operation[+,-,*,/]: ")
    if op=="+" :
        print(add(n1,n2))
    elif op=="-":
        print(sub(n1,n2))
    elif op=="*":
        print(multiply(n1,n2))
    elif op=="/":
        print(divide(n1,n2))
    else:
        print("enter operation is not valid")
        
operation(n1,n2)
