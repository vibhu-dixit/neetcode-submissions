class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)> self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    def insert(self,val):
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=val
        val.prev,val.next=prev,nxt
        
    def remove(self,val):
        val.prev.next=val.next
        val.next.prev=val.prev