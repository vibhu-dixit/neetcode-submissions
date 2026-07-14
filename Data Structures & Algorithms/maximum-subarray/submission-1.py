class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        curr=0
        for num in nums:
            if curr<0:
                curr=0
            curr+=num
            maxsub=max(maxsub,curr)
        return maxsub