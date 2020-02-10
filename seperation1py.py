s="a 1 b 2 c 3 d 4"
#print(s)
s1=s.split()
print(s1)
l=[]
l1=[]
x=0
while x>=len(s1):
    if s1.isdigit():
        l.append(s1(x))
        x=x+1
    elif s1.isalpha():
        l1.append(s1(x))
        x=x+1
    else:
        print("Something is worng")

print(" ".join(l))
print(" ".join(l1))
