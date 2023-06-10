#Pop, pop_first, append and prepend O(1)
#Get, set value, remove(index) and insert(index) O(n)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
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
        #O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        #O(1)
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        temp.prev = None
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
            self.head = None
        return temp

    def prepend(self, value):
        #O(1)
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        #O(1)
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        self.length -= 1
        return temp

    def get(self, index):
        #O(n)
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        #O(n)
        temp = self.get(index)
        if temp:
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
        before = self.get(index - 1)
        after = before.next

        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        #O(n)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()

        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp









my_double_linked_list = DoubleLinkedList(6)
my_double_linked_list.append(8)
my_double_linked_list.append(9)
my_double_linked_list.append(5)
my_double_linked_list.prepend(10)
my_double_linked_list.set_value(1,69)
my_double_linked_list.insert(1,444)
my_double_linked_list.print_list()


