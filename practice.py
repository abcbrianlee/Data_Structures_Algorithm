
def merge(list1, list2):
    i = 0
    j = 0
    combined = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(list):
    if len(list) == 1:
        return list

    midpoint = int(len(list)/2)
    left = merge_sort(list[:midpoint])
    right = merge_sort(list[midpoint:])

    return merge(left, right)

list1 = [5,1,3,8,7,2,6,4]
print(merge_sort(list1))



