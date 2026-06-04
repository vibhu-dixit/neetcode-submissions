class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        vol=0
        while l<r:
            if(heights[l]<heights[r]):
                lower=heights[l]
            else:
                lower=heights[r]
            calc_vol=lower*(r-l)
            vol=max(calc_vol,vol)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return vol
