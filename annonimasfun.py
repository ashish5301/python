#annomies program
print("annomies program")
s=lambda a,b:a+b
a=10
b=20
print(s(a,b))

#bigger value
print("bigger value")
s=lambda a,b: a if a>b else b
a=10
b=20
print(s(a,b))

#filter program
print("filter program")
l=[5,10,15,20]
l1=list(filter(lambda n:n%2==0,l))
print(l1)

#map program
print("map program")
l=[5,10,15,20]
l1=list(map(lambda n:n*n,l))
print(l1)

#map program multiplaction
print("map program multiplaction")
l=[5,10,15,20]
l1=[5,10,15,20]
l2=list(map(lambda l,l1:l*l1,l,l1))
print(l2)

#map program Addition
print("map program Addition")
l=[5,10,15,20]
l1=[5,10,15,20]
l2=list(map(lambda x,y:x+y,l,l1))
print(l2)

#REDUCE program
print("REDUCE program ")
from functools import reduce
l=[5,10,15,20]
l1=[5,10,15,20]
l2=reduce(lambda x,y:x+y,l)
print(l2)


#aliesing
def gret(name):
    print("Hello",name)
gret("ash")
xyz=gret
xyz("sher")
