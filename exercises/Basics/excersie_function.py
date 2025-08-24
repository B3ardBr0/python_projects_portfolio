class HashMap:
    def insert(self, key, value):
        
        
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        pass

    def current_load(self):
        pass

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
