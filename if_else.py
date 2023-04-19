
# elif

num = int(input("enter the value of num:"))
if (num < 0):
    print("Nagative  number")

elif (num == 0):
    print("Number is zero ")
elif(num == 999):
    print("congratulation a win 2000$ ")
else:
    print("the number is positive ")

# Nested list 
x = 20 

if (x < 0):
    print("The number is Nagative")
    
elif(x > 0):
    if ( x <= 10):
        print("number is < 10")

    elif(x > 10 and x <= 20 ):
        print("This is the correct number")
    else : 
        print("the value is greater 20 ")


else:
    print("The is zero")


