class Solution:
    def rob(self, nums: List[int]) -> int:
        def steal(root):
            prev_rob=max_rob=0
            for money in root:
                temp=max(max_rob,prev_rob+money)
                prev_rob=max_rob
                max_rob=temp
            return max_rob
        return max(steal(nums[:-1]),steal(nums[1:]),nums[0])