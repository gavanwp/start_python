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
print(list[7-4])

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


x = m + y 
print("margn",x)





