#A linked list is a type of tree
#Full tree = every node points to 0 nodes or 2 nodes. (no 1-node tree)
#Perfect tree = every level of a tree is maxed out on nodes and is identical on both sides

#Lookup and Remove is O(log N)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contain(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False



my_tree = BinarySearchTree()
my_tree.insert(6)
my_tree.insert(1)
my_tree.insert(59)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.contain(1))