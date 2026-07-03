class Solution:
    def rob(self, nums: List[int]) -> int:
        if_last_chosen=if_last_not_chosen=0

        for money in nums:
            temp=max(if_last_chosen,if_last_not_chosen+money)
            if_last_not_chosen=if_last_chosen
            if_last_chosen=temp
        return if_last_chosen