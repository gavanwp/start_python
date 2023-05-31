# Dictionaries are used to store data values in key:value pairs.
thisdic = {"name": "Gavan",
           "Father": "Anbji",
           "class": "8th"}

print(type(thisdic), thisdic)
print(len(thisdic))
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

# Index
print(thisdic["name"])
print(thisdic["class"])
print(thisdic["Father"])


# Dictionaries cannot have two items with the same key:
a = {"name": "Gavan",
     "age": 12,
     "year": 2000,
     "year": 2004}
print(a["year"])


# The values in dictionary items can be of any data type:
a = {
    "brand": "ford",
    "electric": False,
    "year": 2003,
    "colors": ["red", "green", "yello", "blue"]

}
print(a["colors"])
print(a)

# It is also possible to use the dict() constructor to make a dictionary.
dic = dict(name="Gavan", age=17, clasS=12)
print(dic)

# Access Dictionary Items
# Method No 1 is
items = {"name": "Gavan",
         "age": 12,
         "birth date": 2004}

print(items["name"])
print(items["age"])
print(items["birth date"])

#  NO 2 using Get()
print(items.get("name"))
print(items.get("age"))
print(items.get("birth date"))


# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(car.keys())
a = car.keys()
print(a)
car["year"] = 200
print(car)


# Get Values
# The values() method will return a list of all the values in the dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

b = car.values()
print(b)

car["year"] = 200
print(b)

# The items() method will return each item in a dictionary, as tuples in a list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

a = car.items()
print(a)
car["year"] = 2000
print(car)


# To determine if a specified key is present in a dictionary use the in keyword:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "year" in car:
    print("Yes")
else:
    print("No")


#  Change Dictionary Items
# You can change the value of a specific item by referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2000
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.update({"brand":"Gavanwp"})
print(thisdict)


# Adding Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["cost"] = "200$"
print(thisdict)


dic = {233: "Roshan",
       234 : "Naresh", 
       235 : "Gavan",
       236:"Zakir", 
       237:"Neha"}

print(dic[233])
print(dic[234])
print(dic[237])
print(dic.get(233))

print(dic.items())
for key , value in dic.items():
    print(f"The value of corresponding to the key {key} is {value}")


# POP method in puython 
 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "cost": 200,
  "year": 1964

}
thisdict.pop("brand")
print(thisdict)

# popitem will remove last item from this dictionary
thisdict.popitem()
print(thisdict)

# DELETE method in puython

del thisdict["cost"]
print(thisdict)