class RandomizedSet:

    def __init__(self):
        self.nummap={}
        self.numlist=[]

    def insert(self, val: int) -> bool:
        if val not in self.nummap:
            self.nummap[val]=len(self.numlist)
            self.numlist.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.nummap:
            idx=self.nummap[val]
            lastval=self.numlist[-1]
            self.numlist[idx]=lastval
            self.numlist.pop()
            self.nummap[lastval]=idx
            del self.nummap[val]
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(self.numlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()