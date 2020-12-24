nprime = int(input("Enter an integer : "))
print(nprime, "->", end=" ")
for n in range(nprime + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
              break
       else:
           print(n , end=" ")