#Hash tables are very efficient. Chaining means key value pairs that share the same index.
#Chaining can be avoided or reduced by linear probing, meaning that if an index is used, it will move the key value pair
# to the next closes available index.
#Chaining, if it occurs, can have each key value pair linked to each other by linked lists, making it easier to traverse
#Even though there are for loops in the code, setting the size to accomodate the proper number of index (reduce collision)
# will make it very efficient.

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
        #ord(letter) is th ASCE value for each letter. We multiply by 23 bc it is prime.
        #We also % by self.data_map bc it will return value 0 -6.

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        #.__hash method is O(k), where k is length of key
        #If there are no collisions, set is O(1)
        #In worst case scenario, set item is O(n) due to collisions, however this can be reduced if hash size is increased.
        index = self.__hash(key)
        #This creates an index with the key. For ex. 'Shoes' will return an index value of 4.
        if self.data_map[index] == None:
            self.data_map[index] = []
        #This adds an initial bracket to store in lists to only those that do not have anything in them.
        self.data_map[index].append([key, value])

    def get_item(self, key):
        #.__hash method is O(K) where k is length
        #If there are no collisions, get item is O(1)
        #In worst case scenario, get item is O(n) due to collisions, however this can be reduced if hash size is increased.
        index = self.__hash(key)
        #Using the key, it is going to generate an index where key is stored.
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                #Loops through the len of variables inside where the key is stored
                #Does not loop from hash table 0-6.
                if self.data_map[index][i][0] == key:
                    #[i][0] points to key, [i][1] points to value. [i] points to whatever iteration
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range (len(self.data_map)):
            if self.data_map[i] is not None:
                for x in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][x][0])
        return all_keys

def item_in_common(list1, list2):
#This is a common hashtable interview question. Easy and INEFFICIENT route is to write a nested for loop O(n^2).
#This approach is O(n).
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return j
    return None

list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))

my_hash_table = HashTable()
my_hash_table.set_item('Sponge', 500)
my_hash_table.set_item('Scissors', 1000)
my_hash_table.set_item('Napkins', 950)
print(my_hash_table.keys())
my_hash_table.print_table()



