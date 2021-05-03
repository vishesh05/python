#Tupples

tu=("Hello" ,"There", "Good")
su=("Morning",)

print(tu)


#concatination
print(tu+su)

r=("Vishesh",)*3
print(r)

#Convertin list to a tuple

list1=[1,2,3,4]
print(tuple(list1))
print(tuple("Vishesh"))

#looping
ntu=("Viv",)
n=4
for i in range(int (n)):
   ntu=(ntu,)
   print(ntu)
