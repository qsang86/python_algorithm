#한쪽 끝으로 자료를 넣고 반대쪽으로 자료 뺴는 선형구조
#순서대로 처리해야하는 일에 필요
#FIFO
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node


    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "queue is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "queue is empty"
        return self.head.data


    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None


q = Queue()
q.enqueue(3)
print(q.peek())
q.enqueue(4)
print(q.peek())
q.enqueue(5)
print(q.peek())
print(q.dequeue())
print(q.peek())
