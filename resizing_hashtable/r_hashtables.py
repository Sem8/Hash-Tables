# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = [None] * capacity        

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for each_character in string:
        hash = (( hash << 5) + hash) + ord(each_character)
    return hash % max

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
# def hash_table_insert(hash_table, key, value):
    # hash_table.size += 1
    # index = hash(key, hash_table.capacity)
    # node = hash_table.storage[index]

    # if node is None:
    #     hash_table.storage[index] = LinkedPair(key, value)
    #     return
    # prev = node
    # while node is not None:
    #     prev = node
    #     node = node.next
    # prev.next = LinkedPair(key, value)

def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    new_node = LinkedPair(key, value)
    stored_node = hash_table.storage[index]

    if stored_node is None:
        hash_table.storage[index] = new_node
    elif stored_node is not None and stored_node.key == key:
        stored_node.value = value
    else:
        while stored_node.next:
            if stored_node.next.key == key:
                stored_node.next.value = value
                return
            stored_node = stored_node.next
        stored_node.next = new_node


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    if hash_table.storage[index] is None:
        print(f'warning {key} does not have a value')
    elif hash_table.storage[index].key == key and hash_table.storage[index].next is not None:
        hash_table.storage[index] = hash_table.storage[index].next
    elif hash_table.storage[index].key == key and hash_table.storage[index].next is None:
        hash_table.storage[index] = None
    else:
        current_node = hash_table.storage[index]
        next_node = hash_table.storage[index].next
        iterating = True
        while iterating and next_node is not None:
            if next_node.key == key:
                iterating = False
                current_node.next = next_node.next
            else:
                current_node, next_node = next_node, next_node.next
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    node = hash_table.storage[index]
    
    while node is not None and node.key != key:        
        node = node.next

    if node is None:
        return None
    else:        
        return node.value
    # we no longer want to overwrite
    # get index
    # if hash_table.storage[index] == None, nothing to retrieve
    # else if hash_table.storage[index] !empty
        #iterate through linked list until key found (while next is not None)
        # if key NEVER found, nothing to retrieve

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
