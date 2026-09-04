class MyHashSet:

    def __init__(self):
        self.cap =  1000000
        self.bucket = [[] for _ in range(self.cap)]

    def add(self, key: int) -> None:
        idx = key% self.cap
        
        if key not in self.bucket[idx]:
            self.bucket[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.cap
        if key in self.bucket[idx]:
            self.bucket[idx].remove(key)

        
    def contains(self, key: int) -> bool:
        idx = key % self.cap
        return key in self.bucket[idx]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)