a = lambda x:x*x*x
# (aprint(55))
print(a(3))
list1 = [2,34,5,6,7,8]
null1 = []
for i in list1:
    null1.append(a(i))
print(null1)
# Using Map function we can get the cupe 
new = list(map(a,list1))
print(new)



def add(x):
    return x*x*x

print(add(55))

list2 = [55,66,77,88]
null2 = []
for i in list2:
    null2.append(add(i))
print(null2)

#FILTER FUNCATION 

newlist = [3,4,5,6,7,3,8]

def add(a):
    return a > 5 # True or False


a = list(filter(add,newlist)) #3,4,5,6,7,3,8
print(a)


# I have try these function uing lambda function 

from functools import reduce
a = [2,3,4,6,7]
# 2+3 = 5+4=9+6=15+7=22

sum1 = reduce(lambda x ,y:x+y, a)
print(sum1)

#  Usig this we can get + ,-,/,* of two value
b = [2,3,4,5,6,7]
def reduce1(x,y):
    return x + y 
result_of_reduce__function = reduce(reduce1,b)
print(result_of_reduce__function)

a = [ 2,3,4,5,6,7]

sum2 = list(filter(lambda x:x > 5, a))
print(sum2)

b = [2,3,4,5,6]

sum3 = list(map(lambda x:x*x*x, b))
print(sum3)


# 'is' vs '==' in Python 
print(a is b) # exact location of object in memory 
print(a == b) # Value 

a = [2,3,4,5,6]
b = [2,3,4,5,6]
print(a is b) # and this return false
print(a == b) # this return true 

a = 3
b = 3 
print(a is b) # True
print(a == b) # True

a = "Gavan"
b = "Gavan"
print(a is b) # True
print(a == b)  # True
a = (2,3,4,5)
b = (2,3,4,5)
print(a is b) # True
print(a == b) # True

