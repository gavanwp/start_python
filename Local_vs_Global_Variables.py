a = 10
print("Global variables" , " " ,a)

def add(): 
    global a
    a = 50
    print("This is a global variables" , "" ,a)
    b = 20
    print("local variables " , " ", b)


print("Global variales", "" ,a)
add()
print("Global variales", ""  ,a)




