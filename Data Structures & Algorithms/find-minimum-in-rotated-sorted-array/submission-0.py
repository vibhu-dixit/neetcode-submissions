class Solution:
    def findMin(self, nums: List[int]) -> int:
      n=len(nums)
      x=max(nums)
      for i,val in enumerate(nums):
        if val ==x:
            t= n-i-1
      return nums[-t]