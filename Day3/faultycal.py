#Design a calculator which will correctly solve all the problems except the following ones :
#	45*3=555  	56+9=77		56/6=4
print("Enter 1 for +, 2 for -, 3 for *, 4 for / ")
b = input()
num1= int(input("Enter 1st value"))
num2=int(input("Enter 2nd value"))

if num1==56 and num2==9:
    print("77")
elif num1==45 and num2==3:
    print("555")
elif num1==56 and num2==6:
    print("4")
elif b==1:
    print(num1+num2)
elif b==2:
    print(num1-num2)
elif b==3:
    print(num1*num2)
elif b==4:
    print(num1/num2)
    
    
    
