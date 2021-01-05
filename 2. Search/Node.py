class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first_node = Node(5)
sec_node = Node(12)
first_node.next = sec_node

