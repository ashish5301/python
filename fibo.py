n = int(input("Enter Value For n:"))
a, b = 0, 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibo sequence upto",n,":")
   print(a)
else:
   print("Fibo sequence:",end=" ")
   while count < n:
       print(a,end=" ")
       temp = a + b
       #update values
       a = b
       b = temp
       count += 1
