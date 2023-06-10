#array - data is physically stored next to each other (contiguous) which allows for more efficient access to elements O(1) when retrieving data.
#Because the data is contiguous, arrays have to be fixed-size upon initiation.  Their size generally cannot be changed without creating a new array.

#List - data is non-contiguous, meaning that they are not stored next to each other and have pointers that reference their structure, which costs more data overhead.
#Since they are non-contiguous, they can be adjusted and change their size.

new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)

        break
#Access - constant time
#Appending - Constant time

#Insert - linear runtime
#Delete - linear runtime
