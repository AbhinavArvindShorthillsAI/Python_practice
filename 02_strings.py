class StringOperations:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
    
    # Printing strings
    def print_strings(self):
        print("String 1:", self.str1)
        print("String 2:", self.str2)
    
    # String Indexing
    def string_indexing(self):
        print("First character:", self.str1[0])  # First character
        print("Last character:", self.str1[-1])  # Last character
    
    # String Slicing
    def string_slicing(self):
        print("Slice [0:5]:", self.str1[0:5])  # 'Hello'
        print("Slice [:5]:", self.str1[:5])    # 'Hello'
        print("Slice [7:]:", self.str1[7:])    # 'World!'
        print("Slice [-6:]:", self.str1[-6:])  # 'World!'
    
    # String Length
    def string_length(self):
        print("Length of str1:", len(self.str1))
    
    # Various String Methods
    def string_methods(self, text):
        print("Uppercase:", text.upper())  # Converts to uppercase
        print("Lowercase:", text.lower())  # Converts to lowercase
        print("Capitalize:", text.capitalize())  # Capitalizes first letter
        print("Title:", text.title())  # Capitalizes first letter of each word
        print("Strip:", text.strip())  # Removes leading/trailing spaces
        print("LStrip:", text.lstrip())  # Removes leading spaces
        print("RStrip:", text.rstrip())  # Removes trailing spaces
        print("Replace:", text.replace("World", "Python"))  # Replace substring
    
    # String Split and Join
    def string_split_join(self, text):
        words = text.split(",")  # Splits string into a list
        print("Split:", words)
        print("Join:", " ".join(words))  # Joins list into a string
    
    # String Search and Count
    def string_search_count(self, text):
        print("Find 'World':", text.find("World"))  # Finds first occurrence
        print("Index 'World':", text.index("World"))  # Index of first occurrence
        print("Count of 'a':", text.count("a"))  # Counts occurrences of 'a'
    
    # String Checks
    def string_checks(self, text):
        print("Starts with 'Hello':", text.startswith("Hello"))
        print("Ends with '!':", text.endswith("!"))
        print("Is Digit:", text.isdigit())  # Checks if only digits
        print("Is Alpha:", text.isalpha())  # Checks if only alphabets
        print("Is Alphanumeric:", text.isalnum())  # Checks if alphanumeric
        print("Is Lowercase:", text.islower())
        print("Is Uppercase:", text.isupper())
    
    # String Formatting
    def string_formatting(self, name, age):
        print(f"My name is {name} and I am {age} years old.")  # f-string
        print("My name is {} and I am {} years old.".format(name, age))  # format method
        print("My name is %s and I am %d years old." % (name, age))  # % formatting


# Execution
if __name__ == "__main__":
    str_demo = StringOperations("Hello, World!", "Python Programming")
    
    print("\nString Operations:")
    str_demo.print_strings()
    str_demo.string_indexing()
    str_demo.string_slicing()
    str_demo.string_length()
    
    print("\nString Methods:")
    str_demo.string_methods("   hello world   ")
    
    print("\nString Split & Join:")
    str_demo.string_split_join("apple,banana,orange")
    
    print("\nString Search & Count:")
    str_demo.string_search_count("Hello, World!")
    
    print("\nString Checks:")
    str_demo.string_checks("Hello, World!")
    
    print("\nString Formatting:")
    str_demo.string_formatting("Alice", 25)
