# binary search algorithms HAVE to be sorted
# Time complexity is (log n) due to the while loop iterating through all possibilities and the midpoint being adjusted to half the value of first + last.
# Space complexity is constant O(1) because we recycle and redefine variables 'first' and 'last' and 'midpoint'.
def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            #list[midpoint] > target:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 8)
verify(result)
