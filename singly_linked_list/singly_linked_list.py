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
        if self.tail is None:
            return None
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length = self.length -1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_tail = self.tail
            self.tail = current_node
            current_node.next = None
            self.length = self.length -1
            return current_tail.value

    def add_to_head(self, value):
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value, self.head)
            self.head = new_node
            self.length += 1


    def remove_at_index(self, index):
        if index >= self.length:
            return None
        prev_Node = self.head
        for i in range(index -1):
            prev_Node = prev_Node.next
        target = prev_Node.next
        prev_Node.next = target.next
        target.next = None
        self.length = self.length - 1
        return target.value
