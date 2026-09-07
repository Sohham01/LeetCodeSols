class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        rows,cols=len(grid),len(grid[0])
        cnt=0
        rotten=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                elif grid[r][c]==1:
                    cnt+=1
        mins=0
        dirc=[(1,0),(-1,0),(0,1),(0,-1)]
        while rotten and cnt>0:
            mins+=1
            for i in range(len(rotten)):
                r,c=rotten.popleft()
                for dr,dc in dirc:
                    row,col=r+dr,c+dc
                    if row<0 or row==rows or col<0 or col==cols:
                        continue
                    if grid[row][col]==0 or grid[row][col]==2:
                        continue
                    cnt-=1
                    grid[row][col]=2
                    rotten.append((row,col))
        return mins if cnt==0 else -1