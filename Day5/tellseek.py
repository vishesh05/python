f = open("fy")
f.tell()    #tells aboiut file pointer
print(f.readlines())

print(f.readlines())
f.seek(10)  # change the file pointer
print(f.readlines())