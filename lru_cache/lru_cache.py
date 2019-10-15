from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.di = {}
        self.limit = limit
    
    """Retrieves the value associated with the given key."""
    def get(self, key):
        if key in self.di:
            val = self.di[key]
            current = self.storage.head
            while current:
                if current.value != val:
                    current = current.next
                self.storage.move_to_front(current)
                return self.di[key]
        else:
            return None

    """adds to our dict and DLL"""
    def set(self, key, value):
        if len(self.storage) == 10:
            self.storage.delete(self.storage.tail)
        if key in self.di:
            print(f'its here!! {self.di[key]}')
            self.di[key] = value
            current = self.storage.head
            while current:
                if current.value != self.di[key]:
                    current = current.next
            self.storage.move_to_front(current)
        else:
            #create key, move to front
            self.di[key] = value
            self.storage.add_to_head(value)

valu = 'item 1'
jim = LRUCache()
jim.set(valu, 'a')
print(jim.di)
print(jim.get(valu), f'here is {valu}')
jim.set(valu, 'flenderson')
print(jim.get(valu), f'here is {valu}')

