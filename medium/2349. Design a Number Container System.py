class NumberContainers:

    def __init__(self):
        self.hash=defaultdict(SortedSet)
        self.indexes={}

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            prev=self.indexes[index]
            self.hash[prev].remove(index)
            if not self.hash[prev]:
                    del self.hash[prev]
        self.indexes[index]=number
        self.hash[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.hash or not self.hash[number]:
            return -1
        return self.hash[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
