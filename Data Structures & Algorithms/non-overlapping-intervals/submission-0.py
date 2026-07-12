class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda t:t[0])
        res=0
        last=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=last:
                last=end
            else:
                res+=1
                last=min(end,last)
        return res