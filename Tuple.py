# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])
print(thistuple[1])
print(thistuple[2])
print("Negative Indexing :",thistuple[-2])

# Tuple Length
# To determine how many items a tuple has, use the len() function:
i = (1,2,3,4,5,6,7,8,9)
print(i)
print(len(i))
# I want to create a tuple with only one items
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
i = ("hello",)
print(i)


# Tuple items can be of any data type:
y = ("Roshan", "Naresh","Pardeep")
y1 = (12,3,45,)
y2 = (True,False)

# A tuple can contain different data types:
items = ("Hello world",12,True)
print(items)


# It is also possible to use the tuple() constructor to make a tuple. 
a = ("hello", (True))
print(a)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:6])
print(thistuple[:4])
print(thistuple[4:])

# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-5:-2])


# Check if Item Exists
# To determine if a specified item is present in a tuple using the "in" keyword:
check = ("Roshan","Gavan","Naresh")
if "Roshan" in check :
    print("Yes")
else:
    print("NO")



# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple1 = ("Roshan","Pardeep","Naresh")
print(tuple1)
tuple2 = list(tuple1)
print(tuple2)
tuple2[2] = "Gavan"
print(tuple2)
tuple1 = tuple(tuple2)
print(tuple1)


# Add Items using apend method 
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple
# Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

items = ("Gavan","Roshan","pardep")
print( "Add Items", items)

items1 = list(items)
print( "Now it is changed into list ", items1)
items1.append("Naresh")
print(items1)
items = tuple(items1)
print(items)

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)





