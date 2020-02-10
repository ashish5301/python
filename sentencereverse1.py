s="learning python is Hard"
print(s)
s1=s.split()
l=[]
x=0
while x<len(s1):
    l.append(s1[x][::-1])
    x=x+1
print(" ".join(l))
