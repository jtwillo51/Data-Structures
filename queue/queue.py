"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# ARRAY - passing
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.items = []
#         # self.storage = ?

#     def __len__(self):
#         self.size = len(self.items)
#         return self.size

#     def enqueue(self, value):
#         self.items.insert(0, value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             return self.items.pop()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



class Queue:
    def __init__(self):
        self.size = 0
        self.head: Node = None

        # self.storage = ?

    def __len__(self):
        return self.size

    def enqueue(self, value):
        newNode = Node(value)
        self.size += 1
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def dequeue(self):
        if self.head is None:
            return None
        else:
            self.size = self.size - 1
            temp = self.head
            element = temp.data
            self.head = temp.next
            temp = None
            return element
