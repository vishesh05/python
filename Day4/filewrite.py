# it rewrite the whole file
# f= open("fi", "w")
# for adding text we use "a"

#f = open("fi", "a")
#a = f.write("Idk hii\n")
#print(a)
#f.close

# for read and write mode

f = open("fi", "r+")

print(f.read())
f.write("Trying to read and writ the file \n")
f.close