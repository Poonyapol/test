n= int(input("Enter Number: "))
j = 1
for j in range(n+1):
    if j % 2 != 0:
        k = (n-j)//2
        print(" "*k+"*"*j+" "*k,end="\n")
x = 1
for x in range(n-1,0,-1):
    if x % 2 != 0:
        z = (n-x)//2
        print(" "*z+"*"*x+" "*z,end="\n")