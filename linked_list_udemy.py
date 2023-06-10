#Append, prepend, pop_first O(1)
#pop, Get, set value, remove(index) and insert(index) O(n)

#Linked List - Does not have indices, however they get referenced by head and tail structure (beginning and end of structure)
#Linked list however are not used in real-time practices, rather they help develop algorithmic learning
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        #Adds an item at end of linked list
        #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        #O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        #O(n)
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while(temp.next):
            #While temp.next is true
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        #O(1)
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        #O(n)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        #o(n)
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        #O(n)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        #O(n)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        return temp
        self.length -= 1

    def reverse(self):
        #O(n)
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range (self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after






my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.prepend(77)
my_linked_list.set_value(0,69)
my_linked_list.insert(3, 242424)
my_linked_list.reverse()
my_linked_list.print_list()