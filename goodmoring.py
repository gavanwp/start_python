import time 
a = time.strftime("%H:%M:%S")
print(a)
a = int(time.strftime("%H"))
print(a)

if (a >= 6 and a <= 10 ):
    print("Good Morning")
elif ( a >= 11 and a <= 2):
    print("Good afternoon")
elif(a > 6 and a < 22):
    print("Good evening")

else:
    print("Good Night")


# I hve solved this task 



