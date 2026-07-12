class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #case 1= right ka start<=left ka end<=right ka end, then we merge->left ka start and right ka end
        #case 2= right ka start<=left ka end>right ka end, we keep right ka left ka start and end
        
        intervals.sort(key=lambda t:t[0])
        res=[intervals[0]]
        for start, end in intervals:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res