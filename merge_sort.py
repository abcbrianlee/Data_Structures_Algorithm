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
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(my_list):
    #Merge_sort is very complicated. If you have a list [2,4,1,5,6,4] and use merge sort. Calling it for the first time we will refer to it as the original call stack.
    #First, mid_index is 3 and left becomes [2,4,1]. Dont focus on doing right until left is all the way finished.
    #Next, merge_sort is called on [2,4,1]. This is referred to as the 2nd call stack for the left side. index is 3/2=1.5 ->1. so [2,4,1] gets broken into left=[2] and right=[4,1].
    #Dont focus on right (4,1) yet. Since left[2] is == 1, it gets returned. Now, go to previous right[4,1] and merge_sort.
    #left becomes 4. it then gets sorted. Since that is done, now go to previous right ([1]) and sort. since it is also ==1, it get sorted.
    #Now you have both Left and Right done. (Not on the original merge_sort, but on the 2nd call stack of merge sort). Since oyu have left and right, you can run merge([2], [4,1]).
    #Running merge will set Left=[1,2,4] for the 'Original' call stack.

    #Now you can start on the original call stack on the right.
    #right = [5,6,3]. merge_sort that (2nd call stack on the right) and left = [5] and right =[6,3]. Merge_sort [5] and that gets sorted. Now return to [6,3]. Left = 6 and right = 3. Left gets sorted first. Since its ==1,
    #it gets sorted. Now return back a step to right and sort right = [3]. Since [3] ==1. it gets sorted.
    #Now you have finally sorted the original right and can run merge([5], [6,3]) = [3,5,6]

    #Finally, you can run merge(left, right) on the original call stack as merge([1,2,4] and [3,5,6]) to get final answer =[1,2,3,4,5,6]
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