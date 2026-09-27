class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keysvalues = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.keysvalues:
            self.keysvalues.move_to_end(key)
            return self.keysvalues[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keysvalues and len(self.keysvalues) + 1 > self.capacity:
            self.keysvalues.popitem(last=False)

        self.keysvalues[key] = value
        self.keysvalues.move_to_end(key)
        


        
