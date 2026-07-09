class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])
        res,minheap=[],[]
        curr_i,time=0,tasks[0][0]
        while minheap or curr_i<len(tasks):
            while curr_i<len(tasks) and time>=tasks[curr_i][0]:
                heapq.heappush(minheap,[tasks[curr_i][1],tasks[curr_i][2]])
                curr_i+=1
            if not minheap:
                time=tasks[curr_i][0]
            else:
                processtime,index=heapq.heappop(minheap)
                time+=processtime
                res.append(index)
        return res