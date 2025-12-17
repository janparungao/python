class HashTable:
    def __init__(self):
        self.collection = {}
        
    def hash(self, string: str):
        if not isinstance(string,str):
            raise TypeError("string must be a string")
        result = 0
        for c in string:
            result += ord(c)
        return result
    
    def add(self, key, value):
        hashed = self.hash(key)
        if hashed in self.collection:
            self.collection[hashed][key] = value
        else:
            self.collection[hashed] = {key: value}
    
    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
            self.collection[hashed].pop(key)
    
    def lookup(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
            return self.collection[hashed][key]
        else:
            return None