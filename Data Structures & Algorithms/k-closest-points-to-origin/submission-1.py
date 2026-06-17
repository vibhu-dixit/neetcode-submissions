class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res,minheap=[],[]
        for x,y in points:
            distance=-(x**2 + y**2)
            heapq.heappush(minheap,[distance,x,y])
            if len(minheap)>k:
                heapq.heappop(minheap)
        while minheap:
            dist,x,y=heapq.heappop(minheap)
            res.append([x,y])
        return res