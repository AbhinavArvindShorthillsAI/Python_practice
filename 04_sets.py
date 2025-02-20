# Creating a set
my_set = {1, 2, 3, 4, 5}

# Creating an empty set (Must use set() instead of {})
empty_set = set()
print(empty_set)  # Output: set()








#common set methods
# 1. Adding an element to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# 2. Removing an element (raises KeyError if not found)
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# 3. Removing an element using discard() (does not raise error if not found)
my_set.discard(10)  # No error even if 10 is not in the set

# 4. Removing a random element using pop()
removed_element = my_set.pop()
print(removed_element, my_set)

# 5. Checking if an element exists
print(2 in my_set)  # Output: True
print(10 in my_set)  # Output: False

# 6. Finding Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

# 7. Finding Intersection of two sets
print(set1.intersection(set2))  # Output: {3}

# 8. Finding Difference (elements in set1 but not in set2)
print(set1.difference(set2))  # Output: {1, 2}

# 9. Finding Symmetric Difference (elements in either set, but not both)
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# 10. Checking if a set is a subset of another
print({1, 2}.issubset(set1))  # Output: True


# 11. Updating a set with another set (like union but modifies original set)
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# 12. Clearing a set
set1.clear()
print(set1)  # Output: set()






