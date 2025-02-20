# String Declaration
str1 = "Hello, World!"
str2 = 'Python Programming'

# Printing Strings
print(str1)
print(str2)

# String Indexing (0-based)
print(str1[0])   # First character ('H')
print(str1[-1])  # Last character ('!')

# String Slicing
print(str1[0:5])   # 'Hello' (characters from index 0 to 4)
print(str1[:5])    # 'Hello' (start from 0 up to index 4)
print(str1[7:])    # 'World!' (from index 7 to end)
print(str1[-6:])   # 'World!' (negative indexing)

# String Length
print(len(str1))   # Returns length of string

#The various string methods which are used 

# 1. upper() - Converts string to uppercase
text = "hello"
print(text.upper())  # Output: "HELLO"

# 2. lower() - Converts string to lowercase
text = "HELLO"
print(text.lower())  # Output: "hello"

# 3. capitalize() - Capitalizes first letter
text = "python"
print(text.capitalize())  # Output: "Python"

# 4. title() - Capitalizes first letter of each word
text = "hello world"
print(text.title())  # Output: "Hello World"

# 5. strip() - Removes leading and trailing spaces
text = "   hello world   "
print(text.strip())  # Output: "hello world"

# 6. lstrip() - Removes leading spaces
print(text.lstrip())  # Output: "hello world   "

# 7. rstrip() - Removes trailing spaces
print(text.rstrip())  # Output: "   hello world"

# 8. replace() - Replaces a substring with another
text = "Hello, World!"
print(text.replace("World", "Python"))  # Output: "Hello, Python!"

# 9. split() - Splits string into a list based on delimiter
text = "apple,banana,orange"
print(text.split(","))  # Output: ['apple', 'banana', 'orange']

# 10. join() - Joins list elements into a string
words = ["Python", "is", "awesome"]
print(" ".join(words))  # Output: "Python is awesome"

# 11. find() - Finds first occurrence of a substring
text = "Hello, World!"
print(text.find("World"))  # Output: 7 (index where "World" starts)

# 12. index() - Similar to find(), but raises an error if not found
print(text.index("World"))  # Output: 7

# 13. count() - Counts occurrences of a substring
text = "banana"
print(text.count("a"))  # Output: 3

# 14. startswith() - Checks if string starts with a specific prefix
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True

# 15. endswith() - Checks if string ends with a specific suffix
print(text.endswith("!"))  # Output: True

# 16. isdigit() - Checks if string contains only digits
text = "12345"
print(text.isdigit())  # Output: True

# 17. isalpha() - Checks if string contains only alphabets
text = "Python"
print(text.isalpha())  # Output: True

# 18. isalnum() - Checks if string contains only alphabets and numbers
text = "Python123"
print(text.isalnum())  # Output: True

# 19. islower() - Checks if all characters are in lowercase
text = "hello"
print(text.islower())  # Output: True

# 20. isupper() - Checks if all characters are in uppercase
text = "HELLO"
print(text.isupper())  # Output: True


# f-strings (Recommended way for formatting in Python 3.6+)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 25 years old."

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# Using % operator (Old style, not recommended)
print("My name is %s and I am %d years old." % (name, age))

