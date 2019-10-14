from doubly_linked_list import DoublyLinkedList
import sys


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        self.size -= 1
        return self.storage.remove_from_head()


    def len(self):
        if self.size > 0:
            return self.size
        else:
            return 0

j = Stack()
print(j.push(101))
print(j.push(106))
print(j.len())
print(j.pop())