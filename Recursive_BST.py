def r_contains(self,value):
    return self.__r_contains(self.root, value)

def __r_contains(self, current_node, value):
    if current_node == None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)