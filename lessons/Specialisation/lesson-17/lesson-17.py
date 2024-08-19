# Node class
# A node is where data is stored in the LL
# Each node also holds a pointer which is reference to the next node in the list

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # Get method to return the data stored in the node
    def get_data(self):
        return self.data

    # Get method to return the next node
    def get_next_node(self):
        return self.next_node

    # Set method to set the reference to the next node in the list
    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

# LinkedList class
# This implementation includes the following methods:
# Insert: inserts a new node into the list
# Size: Returns the size of the list
# Traverse/search: Searches list for a node containing the requested data
# Delete: Searches list for a node containing the requested data and removes the node if found
class linked_list:
    # Initializes the linked list with an optional head node
    # If no head is provided, the linked list starts as empty
    def __init__(self, head=None):
        self.head = head

    # String representation of a linked list
    # Provides a string format of the list
    # Traversing the list, collecting each nodes data
    # Return a string showing the data in each node connected by arrows
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        nodes.append("None")
        return "->".join(nodes)

    # Insert: inserts a new node at the beginning of the list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node # Updating the head to this new node

    # Size: Returns the size of the list
    # Traverse the linked list from the head to the end
    # Count the number of nodes
    # Returns the total count/size
    def size(self, data):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.get_next_node()
        return counter

    # Traverse/search: Searches list for a node containing the requested data
    def search(self, data):
        current = self.head
        is_found = False
        while current and is_found is False:
            if current.get_data() == data:
                is_found = True
            else:
                current = current.get_next_node()
        if current is None:
            raise ValueError("Data is not in the list")
        return current

    # Delete
    # Searches for the node within the specified data
    # If found, it removes the node from the list, adjusting the next_node pointer
    # If the node to be deleted is the head node, update the head node with the next node
    def delete(self, data):
        current = self.head
        previous = None
        is_found = False
        while current and is_found is False:
            if current.get_data() == data:
                is_found = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError("Data is not in the list")
        if previous is None:
            self.head = current
        else:
            previous.set_next_node(current.get_next_node)

# Implementation
my_list = linked_list()
print(my_list) # Output: None

node_1 = Node(5)
my_list.head = node_1
print(my_list) # Output: 5->None

node_2 = Node(10)
node_3 = Node(15)

node_1.set_next_node(node_2)
node_2.set_next_node(node_3)

print(my_list) # Output: 5->10->15->None

