class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    A list that may not be necessary
    """


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity=128):
        self.capacity = capacity
        self.storage = self.capacity * [None]

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211  # (0x100000001b3)

        hash = FNV_prime
        for byte in key:
            hash *= FNV_prime
            hash = hash ^ ord(byte)  # ord = unicode location of the byte
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        TODO: Not implemented, optional.
        """

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def add_to_list(self, key, value):
        pass

    def get_from_list(self, key):
        pass

    def remove_from_list(self, key):
        pass

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        index = self.hash_index(key)
        if self.storage[index] == None:
            self.storage[index] = HashTableEntry(key, value)
        else:
            print("Collision")
            # TODO: parse list first
            self.storage[index].value = value

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        index = self.hash_index(key)
        if self.storage[index] == None:
            print("Warning: No value found at this location!")
        else:
            # TODO: Parse through the list first.
            self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        index = self.hash_index(key)
        if self.storage[index] == None:
            return None
        else:  # TODO: parse through the list.
            list_head = self.storage[index]
            return list_head.value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        pass


### Testing functions follow ###
if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
