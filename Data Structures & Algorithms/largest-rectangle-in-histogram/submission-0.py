class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areamax=0
        stack=[]

        for i,height in enumerate(heights):
            start=i
            while stack and stack[-1][1]>height:
                index,h=stack.pop()
                areamax=max(areamax, h*(i-index))
                start=index
            stack.append((start,height))

        for i, height in stack:
            areamax=max(areamax, height*(len(heights)-i))
        return areamax