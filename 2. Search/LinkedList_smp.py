class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

first_node = Node(5)
sec_node = Node(12)
first_node.next = sec_node

#only need head node
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        self.head

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        #print(cur.data)



    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_all()