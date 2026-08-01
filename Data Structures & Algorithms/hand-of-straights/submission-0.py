class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mapp={}
        if len(hand)%groupSize:
            return False
        for num in hand:
            mapp[num]=mapp.get(num,0)+1
        minheap=list(mapp.keys())
        heapq.heapify(minheap)
        while minheap:
            first=minheap[0]
            for i in range(first,first+groupSize):
                if i not in mapp:
                    return False
                mapp[i]-=1
                if mapp[i]==0:
                    if i !=minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True
        