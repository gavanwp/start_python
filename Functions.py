# gmeant mean
# a = 8
# b = 7
# gemeant = (a*b)/(a+b)*(a-b)+(a/b)
# print(gemeant)

# c = 8
# d = 12
# gemeant1 = (c*d)/(c+d)*(c-d)+(c/d)
# print(gemeant1)


# uisng function
def gmeantcalculate(a, b):
    mean = (a*b)/(a+b)
    print(mean)


def greater(a, b):
    if (a > b):
        print("Fist number  is greater")
    else:
        print("secound number  is greater or equal")


def hello(x, y):
    pass


a = 12
b = 2
greater(a, b)
gmeantcalculate(a, b)


x = 1
y = 20
if (x > y):
    print("Fist number  is greater")
else:
    print("secound number  is greater or equal")
greater(x, y)
gmeantcalculate(x, y)


#  ////
def add(a, b):
    result = (a*b)/(a+b)
    print(result)


a = 40
b = 50
if (a > b):
    print("The value of a is greater then B")
else:
    print("The Value of B is Greater then A")
add(a, b)


# Function Arguments in Python

# Default arguments
def add1(a=10, b=20):
    result1 = a + b
    print(result1)


add1()
add1(b=40)
add1(20, 30)
#


def names(Fname, Lname, fname):
    print(Fname, Lname, fname)


names(Fname="Gavan", Lname="kumar", fname="Anbji")


# Keyword arguments
def add2(a, b):
    result2 = a * b
    print("Keyword arguments", result2)


add2(b=40, a=30)


# Average
def add4(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The Average is ", sum/len(numbers))


add4(38, 47, 5, 60)

# dic


def dic(**name):
    print(name["fname"], name["lname"], name["Fname"])


dic(fname="Gavan", lname="kumar", Fname="Anbji")
