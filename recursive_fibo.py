def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
n = int(input("Enter Value For n:"))
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibo sequence:",end=" ")
   for i in range(n):
       print(recur_fibo(i),end=" ")
