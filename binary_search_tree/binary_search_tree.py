import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import *

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self == None:
            BinarySearchTree(value)
        elif self.value < value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)
        else:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                return self.left.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self == None:
            return False
        elif self.value == target:
            return True
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
            return False
        else:
            if self.left:
                return self.left.contains(target)
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self == None:
            return None
        elif self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        dfts = Stack()
        order = []
        current = node
        dfts.push(current)
        while dfts.len() > 0:
            order.append(dfts.storage.head.value.value)
            dfts.pop()
            if current.right != None:
                dfts.push(current.right)
            if current.left != None:
                dfts.push(current.left)
            if dfts.storage.head != None:
                current = dfts.storage.head.value
        for i in sorted(order):
            print(i)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        bfts = Queue()
        current = node
        bfts.enqueue(node)
        while bfts.len() > 0:
            print(current.value)
            bfts.dequeue()
            if current.left:
                bfts.enqueue(current.left)
            if current.right:
                bfts.enqueue(current.right)
            if bfts.storage.head != None:
                current = bfts.storage.head.value


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        dfts = Stack()
        current = node
        dfts.push(current)
        while dfts.len() > 0:
            print(dfts.storage.head.value.value)
            dfts.pop()
            if current.left:
                dfts.push(current.left)
            if current.right:
                dfts.push(current.right)
            if dfts.storage.head != None:
                current = dfts.storage.head.value


    # STRETCH Goals -------------------------
    # Note: Research may be required
    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        global stacka
        current = node
        stacka.push(current)
        while stacka.len() > 0:
            print(current.value)
            stacka.pop()
            if current.left != None:
                self.pre_order_dft(current.left)
            if current.right != None:
                self.pre_order_dft(current.right)
            if current == None:
                return

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        current = node
        if current.left:
            self.post_order_dft(current.left)
        if current.right:
            self.post_order_dft(current.right)
        print(current.value)



stacka = Stack()
bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print('=====IN ORDER=========')
bst.in_order_print(bst)
print('==========BST=============')
bst.bft_print(bst)
print('=================DFT==========')
bst.dft_print(bst)
print('======RECURSION DFT=======')
bst.pre_order_dft(bst)
print('===== POST ORDER RECURSION=========')
bst.post_order_dft(bst)