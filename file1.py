print("Hello world")
print(4+23/77*23-44)


print(55)
#the new line character “\n” is used to create a new line.
print("hello i am \"gavan kumar\" \n this is my friend roshan")
print("hello",44,23, sep=">" , end="4345\n")
print("new line ")

a = " hello dear friend how are you i hope you are doing well "
print(a[3:4])  # Prints characters starting from 3rd to 5th
print(a[2:]) # Prints string starting from 3rd character
print(a*2) ## Prints string two times
print(a+"Gavan kumar") # Prints concatenated string
 #Python List Data Type

# type of 
a1 = str(23)
print(a1, type(a1))
a2 = int(23) # interger
print(a2 , type(a2))
a3 = float(23)
print(a3 , type(a3))



# Variables - Assign Multiple Values 
b1, b2, b3 = "Gavan", "Roshan", "pardeep"
print(b1, b2 , b3)


# One Value to Multiple Variables
c1 = c2 = c3 = "hello world"
print(c1)
print(c2)
print(c3)


# Unpack a Collection 
# If you have a collection of values in a list . Python allows you to extract the values into variables. This is called unpacking.
family = ("Roshan", "gavan", "Pardeep")
a , b , c = family
print(a)
print(b)
print(c)



