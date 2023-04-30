import time
a = time.strftime("%H:%M:%S")
print(a)
a = int(time.strftime("%H"))
print(a)

if (a >= 6 and a <= 10):
    print("Good Morning")
elif (a >= 11 and a <= 2):
    print("Good afternoon")
elif (a > 6 and a < 22):
    print("Good evening")

else:
    print("Good Night")


# I hve solved this task

# I have solved second task myself

sindhi = int(input("enter your sindhi sub marks"))
english = int(input("enter your english sub marks"))
physics = int(input("enter your phy marks"))
maths = int(input("enter your math marks"))
urdu = int(input("enter your urdu marks"))
total = sindhi + english + physics + maths + urdu
percetage = total/500*100
print("your total marks is", "%", percetage)


if (percetage <= 40 and percetage > 33):
    print(percetage, "%", "D grade")
elif (percetage <= 60):
    print(percetage, "%", "C grade")
elif (percetage <= 70):
    print(percetage, "B Grade")
elif (percetage <= 80):
    print(percetage, "%", "A Grade")
elif (percetage <= 100):
    print(percetage, "%", "A+ Grade")
else:
    print("Enter the correct value")

 # third task
 # Write a program that asks the user to input their age and then prints a message indicating whether they are a child, teenager, or adult based on the following criteria:
# If the user is 12 years old or younger, print "You are a child."
# If the user is between 13 and 19 years old, inclusive, print "You are a teenager."
# If the user is 20 years old or older, print "You are an adult."

age = int(input("enter your age "))
if (age <= 12):
    print("You are a child")
elif (age > 12 and age <= 19):
    print("You are a teenager")
elif (age >= 20 and age < 200):
    print("You are an adult")
else:
    print("Please enter correct age")
    age = int(input("enter your age "))



