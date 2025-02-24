class SetOperations:
    def __init__(self, my_set):
        self.my_set = my_set
    
    # Printing Sets
    def print_set(self):
        print("Set:", self.my_set)
    
    # Adding Elements
    def add_element(self, element):
        self.my_set.add(element)
        print("After Adding Element:", self.my_set)
    
    # Removing Elements
    def remove_element(self, element):
        if element in self.my_set:
            self.my_set.remove(element)
            print(f"After Removing {element}:", self.my_set)
        else:
            print(f"Element {element} not found in set.")
    
    def discard_element(self, element):
        self.my_set.discard(element)
        print(f"After Discarding {element}:", self.my_set)
    
    # Removing Random Element
    def pop_element(self):
        if self.my_set:
            removed_element = self.my_set.pop()
            print("Removed Element:", removed_element, "Remaining Set:", self.my_set)
        else:
            print("Set is empty, cannot pop.")
    
    # Checking Membership
    def check_membership(self, element):
        print(f"Is {element} in set?:", element in self.my_set)
    
    # Set Operations
    def set_operations(self, set1, set2):
        print("Union:", set1.union(set2))
        print("Intersection:", set1.intersection(set2))
        print("Difference (set1 - set2):", set1.difference(set2))
        print("Symmetric Difference:", set1.symmetric_difference(set2))
    
    # Checking Subset
    def check_subset(self, subset):
        print(f"Is {subset} a subset?:", subset.issubset(self.my_set))
    
    # Updating Set
    def update_set(self, another_set):
        self.my_set.update(another_set)
        print("After Update:", self.my_set)
    
    # Clearing Set
    def clear_set(self):
        self.my_set.clear()
        print("Set Cleared:", self.my_set)


# Execution
if __name__ == "__main__":
    set_demo = SetOperations({1, 2, 3, 4, 5})
    
    print("\nSet Operations:")
    set_demo.print_set()
    set_demo.add_element(6)
    set_demo.remove_element(3)
    set_demo.discard_element(10)
    set_demo.pop_element()
    set_demo.check_membership(2)
    set_demo.check_membership(10)
    
    print("\nSet Mathematical Operations:")
    set_demo.set_operations({1, 2, 3}, {3, 4, 5})
    set_demo.check_subset({1, 2})
    
    print("\nSet Modification:")
    set_demo.update_set({7, 8, 9})
    set_demo.clear_set()






