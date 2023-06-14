#O (n log n)
#Merge sort is one of the most efficient comparison based sorting algorithms.  It divides the list into smaller sublets.
# recursively sorts them, and then merges the sorted sublist into a final sublist.
#Python's built in .sorted() function uses a sorting algorithm called Timsort, which is a hybrid of merge sort and insertion sort.

def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
    #These last 2 while loops will combine remainder of list if the lists are uneven sizes
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(my_list):
    #Merge_sort is very complicated. If you have a list [2,4,1,5,6,4] and use merge sort. Calling it for the first time we will refer to it as the original call stack.
    #Once we call merge sort , left = [2,4,1] and right = [5,6,4]
    #Next, we call merge sort again. left = [2] right = [4,1]. Since len[2] == 1, we return [2] and we call merge on it. We then call merge_sort on [4,1]. left = 4 and right = 1
    #we call merge on (4,1) and that gets sorted to [1,4]. we then call merge again on [1,4] and [2] and get [1,2,4] for the original merge_sort call stack.
    #Now we move on to the other side. [5,6,4]. We call merge sort and left = [5] and right = [6,4]. Since left [5] == 1, it gets returned. merge sort gets called on [6,4] and turns into [6] and [4]
    #merge gets called on [6] and [4] to become [6,4]. Then merge gets called on [5] and [6,4] to become [4,5,6].
    #Finally the final merge  gets called on [2,4,1] and [4,5,6] to become [1,2,3,4,5,6]
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

list_a = [1,3,5,7]
list_b = [2,4,6,8]
list_c = [5,1,3,6,2,4]

print(merge_sort(list_c))
print(merge(list_a, list_b))