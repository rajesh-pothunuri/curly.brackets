# Doubly linked list implementation
class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
node1 = DoublyLinkedList(1)
node2 = DoublyLinkedList(2)
node3 = DoublyLinkedList(3)
node4 = DoublyLinkedList(4)

node1.next = node2

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.prev = node3

current_node = node4
while current_node is not None:
    print(current_node.data, "=>")
    current_node = current_node.prev