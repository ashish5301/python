def calculator():
    print("1.addition    2.Substration   3.Multiplaction   4.Division")
    n=int(input("Choose the Arithrmatic Operation:"))
    if n==1:
        add()
    elif n==2:
        sub()
    elif n==3:
        mul()
    elif n==4:
        div()
    else:
        print("Wrong Input")
        
def add():
    a=int(input("Enter value to add a:"))
    b=int(input("Enter value to add b:"))
    x=a+b
    print("Addition:",x)

def sub():
    a=int(input("Enter value to add a:"))
    b=int(input("Enter value to add b:"))
    x=a-b
    print("Substraction:",x)
    
def mul():
    a=int(input("Enter value to add a:"))
    b=int(input("Enter value to add b:"))
    x=a*b
    print("Multiplaction:",x)

def div():
    a=int(input("Enter value to add a:"))
    b=int(input("Enter value to add b:"))
    x=a/b
    print("Division:",x)
     
#main code
print("Calculator")
calculator()
p=int(input("Do You Want To continue More Arithrmatic Opertions?(1:Yes | 2:No)"))
while p<2:
    calculator()
