class HashTable():
    def __init__(self):
        self.max = 100
        self.array = [None for i in range(self.max)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key=key)
        self.array[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key=key)
        return self.array[h]

    def __delitem__(self, key):
        h = self.get_hash(key=key)
        self.array[h] = None


lib = HashTable()

lib["Siddharta"] = "196$"
del lib["Siddharta"]
print(lib["Siddharta"])
