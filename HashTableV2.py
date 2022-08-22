import HashTable as Hash_Table


class HashTable(Hash_Table.HashTable):
    def __init__(self):
        super().__init__()
        
        self.array = [[] for i in range(self.max)]

    def __setitem__(self, key, value):
        h = self.get_hash(key=key)
        found = False

        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                self.array[g][idx] = (key, value)
                found = True
                break

        if not found:
            self.array[h].append((key, value))

    def __getitem__(self,key):
        h = self.get_hash(key=key)
        
        for element in self.array[key]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key=key)
        
        for idx, element in enumerate(self.array[h]):
            if element[0] == key:
                del self.array[h][idx]

obj = HashTable()
obj["link"] = "www."
print(obj.max)
print(obj.array)