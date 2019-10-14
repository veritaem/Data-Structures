import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value): # add to end of list, increment size up
        self.size += 1
        self.storage.add_to_tail(value)


    def dequeue(self): # remove from front, decrease size, return removed value
        self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        if self is not None:
            if self.size <=0:
                return 0
            else:
                return self.size
        else:
            return None



