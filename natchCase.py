# x = int(input("Enter the value of x :"))

# match x : 
#     # if x is 0 
#     case 0:
#         print("x is zero")
#     case 12:
#         print("x is 12")
#     case 40: 
#         print("x is 5")

#     case _ if x > 50:
#         print( " The value of x is ", x)
#     case _ if  x!= 100:
#         print("x is equal to  100" )
#     case _:
#         print(x)



y = int(input("enter the vlaue  "))

match y : 
    case 12: 
        print("The value of y is 12")

    case 20:
        print("The value of y is 20")

    case _ if y < 0 :
        print("The value is nagative")
    case _ :
        print(y)

# Good Morning  assignment using Match Case in python 
import time
a = time.strftime("%H")
print(a)
a = int(time.strftime("%H"))

match a : 
    case 12:
        print("The right now is 12")

    case 20:
        print("The is right now is 20 pm")

    case _ :
        print("Good night")
