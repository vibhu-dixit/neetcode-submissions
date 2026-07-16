class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i): #i is the index of the value we are passing on
            if i>=len(nums):
                res.append(subset.copy())
                return
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #decision to not include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
            