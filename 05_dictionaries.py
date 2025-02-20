# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Printing a dictionary
print(my_dict)



# 1. Accessing a value by key
print(my_dict["name"])  # Output: Alice

# 2. Using get() to avoid KeyError if key is missing
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("gender", "Not Found"))  # Output: Not Found

# 3. Adding a new key-value pair
my_dict["gender"] = "Female"
print(my_dict)  # {"name": "Alice", "age": 25, "city": "New York", "gender": "Female"}

# 4. Updating a value
my_dict["age"] = 26
print(my_dict)  # {"name": "Alice", "age": 26, "city": "New York", "gender": "Female"}

# 5. Removing an item using pop()
my_dict.pop("city")
print(my_dict)  # {"name": "Alice", "age": 26, "gender": "Female"}

# 6. Removing last inserted item (Python 3.7+)
my_dict.popitem()
print(my_dict)  # {"name": "Alice", "age": 26}

# 7.update a key value pair in a dictionary
my_dict.update({"city": "New York"})

# 8. Iterating through a dictionary
for key, value in my_dict.items():
    print(key, ":", value)

# 9. Getting all keys
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# 10. Getting all values
print(my_dict.values())  # Output: dict_values(['Alice', 26])

# 11. Getting all key-value pairs as tuples
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 26)])

# 12. Clearing a dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# 13. Copying a dictionary
my_dict = {"a": 1, "b": 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

# 14. Creating a dictionary using fromkeys()
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "Unknown")
print(default_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}
