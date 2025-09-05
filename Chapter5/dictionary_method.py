empty_dictionary = {} # empty dictionary

marks={
    "Anand": 95,
    "Ravi": 85,
    "Suresh": 75
}
# items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(marks.items())  # dict_items([('Anand', 95), ('Ravi', 85), ('Suresh', 75)])


# 

print(marks.keys())  # dict_keys(['Anand', 'Ravi', 'Suresh'])

print(marks.values())  # dict_values([95, 85, 75])

# update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
print(marks.update({"Anand": 100, "Anurag": 99})) 
  
print(marks.get("Anand2"))  # get method returns the value of the item with the specified key.if the key does not exist, it returns None (or a specified default value).
print(marks["Anand"])  # it is same as above but if the key does not exist, it raises a KeyError.


print(marks.pop("Ravi"))  # removes the item with the specified key name and returns its value.

print(marks.popitem())  # removes the last inserted key-value pair and returns it as a tuple.

print(marks)

