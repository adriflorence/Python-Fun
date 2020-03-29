# String Key Hash Table

# Write a HashTable class that stores strings in a hash table,
# where keys are calculated using the first two letters of the string.

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]
        
        
    # Return the hash value if the string is already in the table.
    # Return -1 otherwise.   
    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] != None:
                if string in self.table[hash_value]:
                    return hash_value
        return -1

    def calculate_hash_value(self, string):
        first = string[:1]
        second = string[1:2]
        value = (ord(first) * 100) + ord(second)
        return value

# TESTS

hash_table = HashTable()
assert hash_table.calculate_hash_value('UDACITY') == 8568

# Test lookup edge case
assert hash_table.lookup('UDACITY') == -1

# Test store
hash_table.store('UDACITY')
assert hash_table.lookup('UDACITY') == 8568

# Test store edge case
hash_table.store('UDACIOUS')
assert hash_table.lookup('UDACIOUS') == 8568