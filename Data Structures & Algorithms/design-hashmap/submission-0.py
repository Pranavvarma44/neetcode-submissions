class MyHashMap:

    def __init__(self):
        self.size=1000
        self.buckets=[[] for _ in range(self.size)]
    def hash(self,key):
        return key%self.size

        

    def put(self, key: int, value: int) -> None:
        index=self.hash(key)
        for pairs in self.buckets[index]:
            if pairs[0]==key:
                pairs[1]=value
                return
        self.buckets[index].append([key, value])
        

    def get(self, key: int) -> int:
        index=self.hash(key)
        for pairs in self.buckets[index]:
            if pairs[0]==key:
                return pairs[1]
        return -1
        


    def remove(self, key: int) -> None:
        index = self.hash(key)

        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index].pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)