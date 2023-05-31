

a = 22
b = 22

# if a > b :
#     print("a is greater than b")
# elif a < b :
#     print("a is less than b")
# else :
#     print("a is equal to b")


print("a less than b") if a < b else print("=") if a == b else print("a is greater than b")


# 
c = 10 if a > b else ""
print(c)




#Enumerate Function in Python
marks = [22,31,54,65,25,36,99]
# for mark in marks:
#     print(mark)
#     if mark == 99:
#         print(f" Congratulation A+ You got {mark} ")
#     elif mark > 70:
#         print(f" nice  You got {mark}")
#     elif mark > 33:
#         print(f" Good  You got {mark}")
#     else:
#         print(f" Bad  You got {mark}")



for index , mark in enumerate(marks):
    print(marks)
    print(index)
    if index == 6:
        print(f" Congratulation Gavan  A+ You got {mark} ")
    


#

def add1():
   a = "welcome to my code project"
   print(a)


# 
if __name__ == "__main__":
    add1()

