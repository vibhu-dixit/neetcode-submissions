class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        res=r
        def cansplit(mid):
            subarray=0
            current_sum=0
            for n in nums:
                current_sum+=n
                if current_sum>mid:
                    subarray+=1
                    current_sum=n
            return subarray+1<=k
        while l<=r:
            mid= l + (r-l)//2
            if cansplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        