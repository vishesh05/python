print("Enter 1st numb")
num1=input()
print("Enter 2 nd number")
num2=input()
try:
    print("The sum of two number is", 
        int(num1)+int(num2))
except Exception as e:
    print(e)



print("Important Message")