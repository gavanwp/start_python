for i in range(5):
    print(i)
else:
    print("No i")


for i in []:
    print(i)
else:
    print("No this is me")


# In while loop
a = 0 
while a < 10:
    print(a)
    a += 1
else:
    print("This is while loop ")



for i in range(10):
    print("iterration number {} in for loop ".format(i + 1))
    if i ==2:
        break
else:
    print("kia yai else statement executed ho gyi ?")

