# UserList is a wrapper around the standard Python list.
# It allows you to subclass and add your own custom methods or
# override existing ones.
#
# UserList: Allows you to create custom list-like classes.
# UserDict: Allows you to create custom dictionary-like classes.
# UserString: Allows you to create custom string-like classes.

# Example: Custom List with some numbers and a Method to Remove All Even Numbers

from collections import UserList

class CustomList(UserList):
    def remove_evens(self):
        self.data = [item for item in self.data if item%2 != 0]

custom_list = CustomList([2, 6, 4, 5, 1, 9, 3, 6, 8, 22, 46])
# Before removing even numbers
print(custom_list)
custom_list.remove_evens()
# After removing even numbers
print(custom_list)