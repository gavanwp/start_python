# String in python
a = "hello world"
print(a)
b = 'In the end, it\'s not the "years" in your life that count.'

print(b)
c = """We cannot solve problems with the kind of thinking we employed when we came up with them.” — ...
“Learn as if you will live forever, live like you will die tomorrow.” — ...
“Stay away from those people who try to disparage your ambitions. ...
“When you give joy to other people, you get more joy in return """
print(b)


e = "hello dear this is gavanwp a python developer "
print(e[0])
print(e[1])
print(e[2])


# For Loop

print("For loop\n")

for che in c:
    print(che)

y = int(input("enter your value"))
x = int(input("enter your value"))
print(y + x)

y1 = y2 = y3 = y4 = "Gavan"
print(y2)
print(y1)
print(y4)


# Strings Slicing and Operations on Strings

a = "This Is My First Blo!!"

print(a.swapcase())


# String Concatenation
a = "Gavan"
b = "kumar"
c = a + " " + b
print(c)


# Format - Strings
age = 20
text = "I am Gavan kumar and my age is {}"
print(text.format(age))

#
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# String formating
a = "I am {1}   i am form {0}"
b = "Gavan"
c = "Pakistan"
print(a.format(c, b))


# f_string
# a = input("enter your name")
# b = input("enter your country name")
# print(f"I am {a} i am form {b}")


# price x : . 2f

x = 22.44343
print(f"The Apple price is {x :.2f} dollor")

print(f"{200*300}")
print(f"Hello this is {{name}} string ")


# Docstrings 

def add(a,b):
    '''This is a docstring'''
    a = a + b
    print(a)

add(55,77)
print(add.__doc__)

