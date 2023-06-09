#Sorting algorithms are important because it brings order to unordered data. They arrange elements in a sequence that simplifies further processing or analysis.
#Allows for more efficient searching operations. Algorithms like binary search can be applied because they need to be ordered.
#Bubble sort and Selection sort are highly inefficient, making them not practical in real-time use and only for educational purposes.
def bubble_sort(my_list):
    #Loops through all integers and sorts the highest integer to the last spot first.
    #last final integer gets sorted first, then 2nd to last integer gets sorted next
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


def selection_sort(my_list):
    for i in range(len(my_list)):
    #Iterates through list and finds the smallest integer through comparision
    #Once it finds smallest integer, min_index is set to that index.
    #Then it switches smallest integer with whatever integer is fartest left
    #Sorts it starting with smallest integer, left to right
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
        return my_list

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1


list = [ 4, 6, 5, 1, 3]
print(bubble_sort(list))
print(selection_sort(list))