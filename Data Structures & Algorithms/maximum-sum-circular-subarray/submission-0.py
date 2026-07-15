class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax=globalmin=nums[0]
        currmax=currmin=0
        total=0

        for num in nums:
            currmax=max(currmax+num, num)
            currmin=min(currmin+num, num)
            total+=num
            globalmax=max(globalmax,currmax)
            globalmin=min(globalmin,currmin)
        return max(globalmax,total-globalmin) if globalmax>0 else globalmax