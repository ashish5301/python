s="learning python is Hard"
print(s)
s1=s.split()
#print(s1)
l=[]
x=len(s1)-1
while x>=0:
    l.append(s1[x])
    x=x-1
print(" ".join(l))
