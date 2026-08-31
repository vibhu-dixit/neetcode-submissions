class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit=set()
        q=deque()
        rows,cols=len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0: ## to map the first treasure points
                    q.append((r,c))
                    visit.add((r,c))
        distance=0
        def multibfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==-1 or (r,c) in visit:
                return
            q.append((r,c))
            visit.add((r,c))
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=distance
                multibfs(r+1,c)
                multibfs(r-1,c)
                multibfs(r,c+1)
                multibfs(r,c-1)
            distance+=1