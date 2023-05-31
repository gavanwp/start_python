a  = input("enter your Name")

for ch in a :
    print(ch)

color = ["red", "green", "blue", "yellow", "white", "gray","brown", "pink", "origin"]

for a in color :
    print(a , end=",")


# rang method in for loop

a = "Roshan kumar"
b = a.replace("Roshan", "Gavan")

for y in range(100):
    if (y < 20):
        print("Roshan")
    elif( y < 40):
        print(b.replace("Roshan", "Naresh"))
    elif(y < 60):
        print(b.replace("Naresh","Paredep"))
    elif(y < 80):
        print(b.replace("Naresh", "Gavan"))
    
    else :
        print("error")



# 
for x in range(1, 20, 3):
    print(x)


b = ["roshan", "Gavan","pardeep"]
for b1 in b :
    print(b1)


#  while loop in python
i = 0 
while(i < 20):
    print(i)
    i = i + 1


y = int(input("Enter the value "))
while( y < 40):
    y = int(input("enter the corrct value"))


x = 5 
while(x > 0 ):
    print(x)
    x = x -1 

else: 
    print("i am inside of the else")





