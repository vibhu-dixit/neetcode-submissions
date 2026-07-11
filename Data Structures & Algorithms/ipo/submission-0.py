class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit=[] # prjts we can afford
        mincapital=[ (c,p) for c,p in zip(capital, profits)]
        heapq.heapify(mincapital)

        for i in range(k):
            while mincapital and mincapital[0][0]<=w:
                c,p=heapq.heappop(mincapital)
                heapq.heappush(maxprofit,-p)
            if not maxprofit:
                break
            w+=-heapq.heappop(maxprofit)
        return w