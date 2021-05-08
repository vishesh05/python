a=int(input("Enter a number"))
b=int(input("Enter 0 or 1 :"))
c=bool(b)

if c==True:
    for i in range(0,a):
        for j in range(0,i):
            print("*", end=" ")
        print()
elif c==False:
    for i in range(a,0,-1):
        for j in range(0,i):
            print("*",end="")
        print()