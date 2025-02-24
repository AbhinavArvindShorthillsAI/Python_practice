class ListOperations:
    def __init__(self, my_list, mixed_list, nested_list):
        self.my_list = my_list
        self.mixed_list = mixed_list
        self.nested_list = nested_list
    
    # Printing Lists
    def print_lists(self):
        print("List of Integers:", self.my_list)
        print("Mixed Data Types List:", self.mixed_list)
        print("Nested List:", self.nested_list)
    
    # Accessing List Elements
    def list_indexing(self):
        print("First element:", self.my_list[0])
        print("Last element:", self.my_list[-1])
    
    # List Slicing
    def list_slicing(self):
        print("Slice [1:4]:", self.my_list[1:4])
        print("Slice [:3]:", self.my_list[:3])
        print("Slice [2:]:", self.my_list[2:])
        print("Reversed List:", self.my_list[::-1])
    
    # List Length
    def list_length(self):
        print("Length of List:", len(self.my_list))
    
    # List Methods
    def list_methods(self):
        temp_list = self.my_list.copy()
        temp_list.append(6)
        print("After Append:", temp_list)
        temp_list.extend([7, 8])
        print("After Extend:", temp_list)
        temp_list.insert(2, 99)
        print("After Insert at index 2:", temp_list)
        temp_list.remove(99)
        print("After Removing 99:", temp_list)
        print("Popped Element:", temp_list.pop())
        print("Popped Element at index 1:", temp_list.pop(1))
        print("Index of 4:", temp_list.index(4))
        print("Count of 3:", temp_list.count(3))
        temp_list.reverse()
        print("Reversed List:", temp_list)
        temp_list.sort()
        print("Sorted List:", temp_list)
        sorted_copy = sorted(temp_list)
        print("New Sorted List:", sorted_copy)
        copy_list = temp_list.copy()
        print("Copied List:", copy_list)
        copy_list.clear()
        print("Cleared List:", copy_list)
    
    # List Comprehension
    def list_comprehension(self):
        squares = [x ** 2 for x in range(5)]
        print("Squares using List Comprehension:", squares)
    
    # Additional List Operations
    def additional_operations(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        print("Concatenated List:", list1 + list2)
        print("Repeated List:", list1 * 3)
        numbers = [10, 50, 20, 5]
        print("Max Value:", max(numbers))
        print("Min Value:", min(numbers))
    

# Execution
if __name__ == "__main__":
    list_demo = ListOperations([1, 2, 3, 4, 5], [1, "Hello", 3.14, True], [[1, 2, 3], [4, 5, 6]])
    
    print("\nList Operations:")
    list_demo.print_lists()
    list_demo.list_indexing()
    list_demo.list_slicing()
    list_demo.list_length()
    
    print("\nList Methods:")
    list_demo.list_methods()
    
    print("\nList Comprehension:")
    list_demo.list_comprehension()
    
    print("\nAdditional List Operations:")
    list_demo.additional_operations()

