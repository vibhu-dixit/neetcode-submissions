class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currentsum=0
        prefix={0:1}
        for n in nums:
            currentsum+=n
            dif=currentsum-k
            res+=prefix.get(dif,0)
            prefix[currentsum]=1+prefix.get(currentsum,0)
        return res