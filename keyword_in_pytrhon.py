
def function1():
    try:
        i = [2,3,4,5,6,7,8,9,10,11,12]
        l = int(input("inter the index number "))
        print(i[l])
        return 0 
    except IndexError:
        print("index out of range")
        return 1
    finally:
        print("finally is always executed  in function")



a = function1()
print(a)



# Raising custom errors in Python 


a = int(input("Enter a number between  5 and 8 "))

if a < 5 or a > 8 :
   
    raise ValueError("Number is out of range")

else:
    print(f"Number is in range {a}")




b = input("Enter a number between 5 and 8  or enter quit")

if b == "quit":
    print("goodbye")
elif int(b) < 5 or int(b) > 8 :
    raise ValueError("Number is out of range")
else:
    print(f"Number is in range {int(b)}")