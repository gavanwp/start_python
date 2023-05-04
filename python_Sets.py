# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
thisset = {23, 43, 24, 55, 55, 23, 24}
print(thisset)

# Get the Length of a Set
thisset = {"red", "blue", "green", "yellow", "gray"}
print(len(thisset))


# Set items can be of any data type:
thisset = {"banana", "apple", "cherry"}
thisset = {22, 342}
thisset = {True, False}


# A set can contain different data types:
# A set with strings, integers and boolean values:
thisset = {"Gavan", 22, True}
print(thisset)


# type()
# From Python's perspective, sets are defined as objects with the data type 'set':
thisset = {"Roshan", "Naresh"}
print(type(thisset))


# The set() Constructor
# note the double round-brackets
thisset = set(("banana", "apple", "cherry"))
print(thisset)


# Access Items
thisset = {"green", "yello", "gray"}

for i in thisset:
    print(i)


# check
thisset = {"apple", "banana", "cherry"}
print("apple" in thisset)


# To add one item to a set use the add() method.
thisset = {1, 2, 3, 4, 5}
thisset.add("hello")
print(thisset)

# o add items from another set into the current set, use the update() method.
a = {10, 20, 30, 40}
b = {50, 60, 70}
a.update(b)
print(a)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

x = {"roshan", "naresh"}
y = ["Pardeep", "Gavan"]
x.update(y)
print(x)


# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"Apple", "Banana", "Cherry"}
thisset.remove("Banana")
print(thisset)


# Remove "banana" by using the discard() method:

thisset = {"Roshan", "Naresh", "Gavan"}
thisset.discard("Gavan")
print(thisset)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
thisset = {22, 33, 44, 55, 66, 77}
y = thisset.pop()
print(y)
print(thisset)


# The clear() method empties the set:
thisset = {"green", "yellow", "gray"}
thisset.clear()
print(thisset)


# The del keyword will delete the set completely:
# thisset = {"cherry", "apple"}
# del thisset
# print(thisset)


# LOOP ITEMS
# You can loop through the set items by using a for loop:
thisset = {2, 3, 4, 5, 6}
for i in thisset:
    print(i)


# Python - Join Sets
# You can use the union() method that returns a new set containing
# all items from both sets, or the update() method that inserts all the items from one set into another:
# uisng Update method
a = {"kabul", "Tirana", "Alglers", "Andorra la vella", "luanda"}
b = {"Saint john's", "Buenos Aires", "Yerevan"}
a.update(b)


a = {"kabul", "Tirana", "Alglers", "Andorra la vella", "luanda"}
b = {"Saint john's", "Buenos Aires", "Yerevan"}
capital = a.union(b)
print(capital)


# Set difference() Method
# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

thisset1 = {"Apple", "green", "cherry", "yello"}
thisset2 = {"Cherry", "gray", "Banana", "green"}
result = thisset1.difference(thisset2)
print(result)

# Set difference_update() Method
# The difference_update() method removes the items that exist in both sets.

# The difference_update() method is different from the difference() method, because the difference() method returns a new set,
# without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

a = {"a", "b", "c", "d"}
b = {"a", "d", "c", "e"}
a.difference_update(b)
print(a)

# Set intersection() Method

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)


# Set isdisjoint() Method
# The isdisjoint() method returns True if none of the items are present 
# in both sets, otherwise it returns False.

a = {"red", "green", "yellow"}
b = {"apple", "banana", "cherry"}
c = a.isdisjoint(b)
print(c)


# Set issubset() Method
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Set issuperset() Method
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)