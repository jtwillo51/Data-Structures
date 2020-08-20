class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        newNode = Node(value)
        self.length =+1
        if self.tail is None:
            self.head = newNode
            self.tail = newNode

        else:
           old_tail = self.tail
           old_tail.next = newNode
           self.tail = newNode

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return current_head.value
        else:
            current_head = self.head 
            self.head = current_head.next
            self.length = self.length -1
            return current_head.value
    
    def remove_tail(self):
        current = self.head
        if current != None:
            self.length -= 1
            self.head = current.get_next()
            return self.head.data
        else:
            return None
