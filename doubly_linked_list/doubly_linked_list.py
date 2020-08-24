"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        newNode = ListNode(value)
        # if list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.head.prev = None
            self.tail.next = None
            self.length += 1
            return self.head.value
        else:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
        self.head = newNode
        self.length += 1
        return self.head.value

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            rt_value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return rt_value
        else:
            rt_value = self.head.value
            self.head.next = self.head
            self.head = None
            self.length = self.length - 1
            return rt_value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)\
            # list has no values
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

            # list has 1 value
        elif self.head == self.tail:
            self.head.next = new_node
            new_node.prev = self.head
            self.tail = new_node
            self.length += 1

            # list has many values (General case)
        else:
            old_tail = self.tail
            self.tail = new_node
            self.tail.prev = old_tail
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # empty list
        if self.tail is None:
            return None
        # list with 1 value
        elif self.head == self.tail:
            self.head = None
            rt_value = self.tail
            self.tail = None
            self.length = self.length - 1
            return rt_value.value
        # list with many values (General case)
        else:
            new_tail = self.tail.prev
            rt_value = self.tail
            self.tail = None
            new_tail.next = None
            self.length = self.length - 1
            return rt_value.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            return None
        elif self.head == node:
            return None
        elif self.tail == node:
            new_tail = node.prev
            self.tail = new_tail
            self.tail.next = None
            old_head = self.head
            old_head.prev = node
            self.head = node
            self.head.next = old_head
            node.prev == None
        else:
            prev_node = node.prev
            next_node = node.next
            next_node.prev = prev_node
            old_head = self.head
            old_head.prev = node
            self.head = node
            self.head.next = old_head
            node.prev == None

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            return None
        elif node.next is None:
            return None
        elif node.prev is None:
            self.head = node.next
            old_tail = self.tail
            old_tail.next = node
            self.tail = node
            self.tail.prev = old_tail
        else:
            prev_node = node.prev
            next_node = node.next
            next_node.prev = prev_node
            old_tail = self.tail
            old_tail.next = node
            self.tail = node
            self.tail.prev = old_tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # empty list
        if self.length == 0:
            return None
        # with 1 value
        elif self.head == self.tail:
            rt_value = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return rt_value.value

        elif node == self.tail:
            old_tail = self.tail
            self.tail = old_tail.prev
            rt_value = node.value
            self.length -= 1
            return rt_value
        elif node == self.head:
            old_head = self.head
            self.head = old_head.next
            old_head.prev = None
            rt_value = node.value
            old_head = None
            self.length -= 1
            return rt_value
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            self.head.next = self.tail
            rt_value = node
            node = None
            self.length = self.length - 1
            return rt_value.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            max = self.head.value
            current = self.head
            while(current!= None):
                if(current.value >max):
                    max = current.value
                    current = current.next
                else:
                    current = current.next
            return max