class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        elec=[0,0,0]
        for num in nums:
            elec[num]+=1
        
        idx =0
        for i in range(3):
            while elec[i] != 0:
                elec[i]-=1
                nums[idx]=i
                idx+=1