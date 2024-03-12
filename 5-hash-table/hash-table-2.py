class HashTable:
    def __init__(self, size = 35):
        self.size = size
        self.buckets = [None]*size

    def hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.size

    def has_key(self, key):
        return False if self.get(key) else True
    
    def idx_exists(self, idx):
        return True if idx <= self.size and self.buckets[idx] else False
    
    def validate_key(func):
        def inner(self, key, *args):
            if len(key) == 0:
                raise Exception('Key cannot be an empty string')
            if not isinstance(key, str):
                raise Exception('Key must be a string')
        return inner

    def validate_set(func):
        def inner(self, key, value):
            if len(self.buckets) >= self.size:
                raise Exception('Hash table has reach its buckets limit')
        return inner

    #@validate_key
    #@validate_set
    def set(self, key, value):
        idx = self.hash(key)
        if not self.idx_exists(idx):
            self.buckets[idx] = [key, value]
        else:
            self.buckets[idx][1] = value
    
    #@validate_key
    def get(self, key):
        idx = self.hash(key)
        if self.idx_exists(idx) and self.buckets[idx][0] == key:
            return self.buckets[idx][1]

# Phonebook Example using custom hash table

if __name__ == '__main__':
    phone_book = HashTable(5)

    phone_book.set('jenny', 8675309)
    phone_book.set('emergency', 911)

    print(phone_book.get('jenny'))
    print(phone_book.get('emergency'))