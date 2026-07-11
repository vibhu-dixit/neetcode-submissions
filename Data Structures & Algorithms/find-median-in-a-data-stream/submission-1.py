class MedianFinder:

    def __init__(self):
        self.minheap=[] #inherently max
        self.maxheap=[] #inherently min

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap,-1*num)
        if (self.minheap and self.maxheap and -1*(self.minheap[0])>self.maxheap[0]):
            curr=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-1*curr)
        if len(self.minheap)>len(self.maxheap)+1:
            curr=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-1*curr)
        if len(self.minheap)+1<len(self.maxheap):
            curr=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-1*curr)

    def findMedian(self) -> float:
        if len(self.minheap)>len(self.maxheap):
            return -1 * self.minheap[0]
        if len(self.minheap)<len(self.maxheap):
            return  self.maxheap[0]
        return (-1*(self.minheap[0]) + self.maxheap[0])/2