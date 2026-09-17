class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        rows,cols=len(heights),len(heights[0])
        heap=[(0,0,0)]
        max_eff=0
        visited=set()
        dirn=[(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            eff,r,c=heapq.heappop(heap)
            max_eff=max(max_eff,eff) 
            if (r,c)==(rows-1,cols-1):
                return max_eff
            visited.add((r,c))
            for dr,dc in dirn:
                rr,cc=r+dr,c+dc
                if 0<=rr<rows and 0<=cc<cols and (rr,cc) not in visited:
                    eff=abs(heights[rr][cc]-heights[r][c])
                    heapq.heappush(heap,(eff,rr,cc))
        return max_eff