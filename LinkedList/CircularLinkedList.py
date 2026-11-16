class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node1.prev = node4

node2.next = node3
node2.prev = node1 

node3.next = node4
node3.prev = node2

node4.next = node1
node4.prev = node3 

current_node = node1
loop = 0
while True:
    print(current_node.data, "=>")
    current_node = current_node.next
    if current_node == node1:
        loop += 1
    if loop == 3:
        break
    