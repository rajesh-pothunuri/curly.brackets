# Singly linked list implementation

class Node:
    # create a constructor with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# create a linked list with three nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#assign the next pointer of each node to the next node
node1.next = node2
node2.next = node3

#loop through the linked list and print the data of each node
current_node = node1
while current_node is not None:
    print(current_node.data, "=>")
    current_node = current_node.next
