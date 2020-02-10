def add(a,b):
     x=a+b
     print("Addition:",x)

def sub(a,b):
    x=a-b
    print("Substraction:",x)
    
def mul(a,b):
    x=a*b
    print("Multiplaction:",x)

def div(a,b):
    x=a/b
    print("Division:",x)

def fibo(a):
     i=0
     for i in range(0,a):
          i=i+(i+1)
          print(i,end=" ")
     
#main code
a=int(input("Enter value to add a:"))
b=int(input("Enter value to add b:"))
print("1.addition    2.Substration   3.Multiplaction   4.Division  5.Fibonaci Series")
n=int(input("Choose the Arithrmatic Operation:"))
if n==1:
    print("Add",a,"&",b)
    add(a,b)
elif n==2:
    print("substract",a,"&",b)
    sub(a,b)
elif n==3:
    print("multiply",a,"&",b)
    mul(a,b)
elif n==4:
    print("divide",a,"&",b)
    div(a,b)
elif n==5:
    fibo(a)
else:
    print("Wrong Input")
