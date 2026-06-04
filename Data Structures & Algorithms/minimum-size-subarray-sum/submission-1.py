class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        final=0
        res=float('inf')
        for i in range(len(nums)):
            final+=nums[i]
            while final>=target:
                res=min(i-l+1,res)
                final-=nums[l]
                l+=1
        return 0 if res == float("inf") else res