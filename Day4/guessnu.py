n=20
i=0
print("You Have 5 chance")
while i<5:
    b=int(input("Enter a number"))
    if b>20:
        print("Greater than your guess")
    elif b==n:
        print("You Won")
        exit()
    else:
        print("less than your guess")
    i+=1
if i==5:
    print("Game Over")