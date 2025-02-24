class DictOperations:
    def __init__(self, my_dict):
        self.my_dict = my_dict
    
    # Printing Dictionary
    def print_dict(self):
        print("Dictionary:", self.my_dict)
    
    # Accessing values
    def access_value(self, key):
        print(f"Value for {key}:", self.my_dict.get(key, "Not Found"))
    
    # Adding Key-Value Pair
    def add_entry(self, key, value):
        self.my_dict[key] = value
        print(f"After Adding ({key}: {value}):", self.my_dict)
    
    # Updating Key Value Pair
    def update_entry(self, key, value):
        self.my_dict[key] = value
        print(f"After Updating ({key}: {value}):", self.my_dict)
    
    # Removing an Entry
    def remove_entry(self, key):
        if key in self.my_dict:
            self.my_dict.pop(key)
            print(f"After Removing {key}:", self.my_dict)
        else:
            print(f"Key {key} not found.")
    
    # Removing Last Inserted Entry
    def pop_last_entry(self):
        if self.my_dict:
            self.my_dict.popitem()
            print("After Removing Last Entry:", self.my_dict)
        else:
            print("Dictionary is empty.")
    
    # Updating Multiple Key-Value Pairs
    def update_dict(self, updates):
        self.my_dict.update(updates)
        print("After Updating Dictionary:", self.my_dict)
    
    # Iterating Through Dictionary
    def iterate_dict(self):
        for key, value in self.my_dict.items():
            print(key, ":", value)
    
    # Getting Keys, Values, and Items
    def get_keys_values_items(self):
        print("Keys:", self.my_dict.keys())
        print("Values:", self.my_dict.values())
        print("Key-Value Pairs:", self.my_dict.items())
    
    # Clearing Dictionary
    def clear_dict(self):
        self.my_dict.clear()
        print("Dictionary Cleared:", self.my_dict)
    
    # Copying Dictionary
    def copy_dict(self):
        new_dict = self.my_dict.copy()
        print("Copied Dictionary:", new_dict)
    
    # Creating Dictionary Using fromkeys()
    @staticmethod
    def create_from_keys(keys, default_value):
        new_dict = dict.fromkeys(keys, default_value)
        print("New Dictionary from Keys:", new_dict)


# Execution
if __name__ == "__main__":
    dict_demo = DictOperations({"name": "Alice", "age": 25, "city": "New York"})
    
    print("\nDictionary Operations:")
    dict_demo.print_dict()
    dict_demo.access_value("name")
    dict_demo.access_value("gender")
    dict_demo.add_entry("gender", "Female")
    dict_demo.update_entry("age", 26)
    dict_demo.remove_entry("city")
    dict_demo.pop_last_entry()
    dict_demo.update_dict({"city": "New York", "country": "USA"})
    
    print("\nIterating and Getting Keys, Values, Items:")
    dict_demo.iterate_dict()
    dict_demo.get_keys_values_items()
    
    print("\nClearing and Copying Dictionary:")
    dict_demo.clear_dict()
    dict_demo.copy_dict()
    
    print("\nCreating Dictionary from Keys:")
    DictOperations.create_from_keys(["name", "age", "city"], "Unknown")
