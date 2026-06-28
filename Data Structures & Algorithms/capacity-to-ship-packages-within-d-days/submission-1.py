class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def canship(capacity):
            ship,curcapacity=1,capacity
            for w in weights:
                if curcapacity-w<0:
                    ship+=1
                    curcapacity=capacity
                curcapacity-=w
            return ship<=days
        while l<=r:
            capacity=(l+r)//2
            if canship(capacity):
                res=min(res,capacity)
                r=capacity-1
            else:
                l=capacity+1
        return res