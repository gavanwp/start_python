a = "hello world"
print(a)

list = [33, 53, 64, 64, 34, True, "hello"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[4])
print(list[5])
print(list[6])

# Negative Index
print(list[-4])
print(list[len(list)-4])
print("hello",list[7-4])

#
if 33 in list:
    print("Yes")
else:
    print("NO")


# same thing applies for string as well
# a = "Gavan"
# if "Gava" in "Gavan":
#     print("Yes")
# else:
#     print("no")


list1 = [2, 4, 5, 3, 5, 3]
print(list1[:])
print(list1[1:len(list1)])
print(list1[1:len(list1):2])


# List Comprehension
list =[ i for i in range(30)]
list =[ i for i in range(30) if i%2==0]
print(list)

# List Methods in Python 

l = [ 11, 45, 1, 2,3,4,5,2]
#Method number 01 
l.append(10)
print(l)
#Method number 02
l.sort()
print(l)
#Mthod number 03
l.reverse()
print(l)
#Method number 04
print(l.count(2))

m = l.copy()
# m[0] = 0
print(m)
m.insert(1, 200)
print(m)

# Extend Method in python 
y = [ 30,40,50]
print(y)
m.extend(y)
print(m)


# Change Item Value
# To change the value of a specific item, refer to the index number:
a = [ 20 , 30 ,45,74,34]
a[3] = 50
print(a)

# Change a Range of Item Values
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

a = ["Gavan", "Roshan", "Naresh", "pardeep"]
a[1:] = ("Pardeep", "Roshan", "Raj")
print(a)





# Remove Specified Item 
y = [30, 20,53,23,44]
y.remove(53)
print(y)
# The pop() method removes the specified index.
x = ["apple", "banana", "cherry"]
x.pop(1)
print(x)
# If you do not specify the index, the pop() method removes the last item.
x.pop()
print(x)

# Clear the List
i = ["apple", "banana", "cherry"]
i.clear() 
print(i)


























