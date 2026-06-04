class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       res=[]
       for i,a in enumerate(nums):
        if a>0:
            break # jaisehi humara main number will be more than 0, so aage ke saare 0.
        if i>0 and a == nums[i-1]:
            continue # this is duplicate check
        l,r=i+1,len(nums)-1
        while l<r:
            curr=a+nums[l]+nums[r] # normal 2 pointer approach aa gayi ab
            if curr>0:
                r-=1
            elif curr<0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                r-=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1 # again duplicate check
       return res