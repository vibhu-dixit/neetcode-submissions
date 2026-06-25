class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr=set()
        for x in nums:
            if x in arr:
                return x
            arr.add(x)