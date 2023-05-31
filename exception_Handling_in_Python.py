a = input("enter your value")
print(f"The table of {a}")


try:
 for i in range(1,11):
    print(f"{a} * {i} = {int(a)*int(i)}")

except Exception as e:
    print(e)


print("some important lines of code ")
print("The program is ending")


#using our custom error handler message 
a = input("enter your value")
print(f"The table of {a}")


try:
 for i in range(1,11):
    print(f"{a} * {i} = {int(a)*int(i)}")

except:
    print("invalid table")


print("some important lines of code ")
print("The program is ending")


try :
   num = int(input("Enter a number"))
   a = [6,3]
   print(f"The number is  {a[num]}")

except ValueError:
   print("you entered value is not a integer")
except IndexError:
    print("index error")

