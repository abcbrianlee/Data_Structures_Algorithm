# Lists have indices
#time complexity is O(n) bc the for loop iterates through all elements of the list
#Space complexity is O(1) bc it does not require additional memory allocation that scales with input size
def linear_search(list, target):
    # Returns the index position of the target if found, else returns None
    for i in range(0, len(list)):
        #range function (start-inclusive, end-exclusive)
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 8)
verify(result)
