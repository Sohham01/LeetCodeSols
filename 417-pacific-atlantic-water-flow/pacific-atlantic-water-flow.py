class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        r=len(heights)
        c=len(heights[0])
        dirt=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(i,j,visited):
            visited.add((i,j))
            for di,dj in dirt:
                ii,jj=i+di,j+dj
                if 0<=ii<r and 0<=jj<c:
                    if (ii,jj) not in visited and heights[ii][jj]>=heights[i][j]:
                        dfs(ii,jj,visited)
        atlantic,pacific=set(),set()
        for j in range(c):
            dfs(0,j,pacific)
        for i in range(r):
            dfs(i,0,pacific)
        for j in range(c):
            dfs(r-1,j,atlantic)
        for i in range(r):
            dfs(i,c-1,atlantic)
        return list(atlantic & pacific)