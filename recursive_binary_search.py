#Recursive binary search calls on itself until it achieves target, and then returns answer back to original statement that initially called it
#Each time function calls itself, target list is cut in half.
#Time Complexity is O (log N) bc at each recursive call, the input list is divided in half
#Space complexity is O (log N) bc at each recursive call, the input list is divided in half
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 6)
verify(result)

