"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.items = []

#     def __len__(self):
#         return len(self.items)

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         if len(self.items) == 0:
#             return None
#         else:
#             return self.items.pop()

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self, new_node):
        self.next_node = new_node


class Stack:
    def __init__(self):
        self.size = 0
        self.head: Node = None
        self.tail: Node = None

        # self.storage = ?

    def __len__(self):
        return self.size

    def push(self, value):
        new_item = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_item
        else:
            while self.head.get_next():
                self.head = self.head.get_next()
            self.head.set_next(new_item)
        

    def pop(self):
        current = self.head
        if current != None:
            self.size -= 1
            self.head = current.get_next()
            return self.head.data
        else:
            return None

