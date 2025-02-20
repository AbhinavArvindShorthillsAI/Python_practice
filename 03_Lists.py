# List Declaration
my_list = [1, 2, 3, 4, 5]  # List of integers
mixed_list = [1, "Hello", 3.14, True]  # Mixed data types
nested_list = [[1, 2, 3], [4, 5, 6]]  # Nested lists

# Printing Lists
print(my_list)
print(mixed_list)
print(nested_list)

# Accessing List Elements
print(my_list[0])   # First element (1)
print(my_list[-1])  # Last element (5)

# List Slicing
print(my_list[1:4])   # [2, 3, 4] (index 1 to 3)
print(my_list[:3])    # [1, 2, 3] (start from 0 up to index 2)
print(my_list[2:])    # [3, 4, 5] (from index 2 to end)
print(my_list[::-1])  # Reverse the list [5, 4, 3, 2, 1]

# Length of List
print(len(my_list))  # Output: 5


# 1. append() - Adds an element to the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# 2. extend() - Extends list by adding elements from another list
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 3. insert() - Inserts an element at a specific index
my_list.insert(2, 99)  # Insert 99 at index 2
print(my_list)  # Output: [1, 2, 99, 3, 4, 5, 6]

# 4. remove() - Removes first occurrence of a value
my_list.remove(99)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# 5. pop() - Removes and returns element at given index (default: last)
print(my_list.pop())   # Removes last element (6)
print(my_list.pop(1))  # Removes element at index 1 (2)

# 6. index() - Returns index of first occurrence of an element
print(my_list.index(4))  # Output: 2

# 7. count() - Counts occurrences of a value
print(my_list.count(3))  # Output: 1

# 8. reverse() - Reverses the list in place
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 1]

# 9. sort() - Sorts the list in ascending order
numbers = [5, 3, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 3, 5, 8, 9]

# 10. sorted() - Returns a new sorted list (does not modify original list)
numbers = [5, 3, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 3, 5, 8, 9]
print(numbers)  # Original list remains unchanged

# 11. copy() - Creates a copy of the list
copy_list = numbers.copy()
print(copy_list)  # Output: [5, 3, 8, 1, 9]

# 12. clear() - Removes all elements from the list
copy_list.clear()
print(copy_list)  # Output: []

# 13. list comprehension - Creating list using a loop in one line
squares = [x ** 2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


# List additional functions

# List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)  # Output: [1, 2, 3, 4, 5, 6]

# List Repetition
print(list1 * 3)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Finding Maximum and Minimum in a List
numbers = [10, 50, 20, 5]
print(max(numbers))  # Output: 50
print(min(numbers))  # Output: 5
