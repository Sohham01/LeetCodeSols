class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        provinces=0
        def dfs(city):
            visited.add(city)
            for curr,connected in enumerate(isConnected[city]):
                if connected and curr not in visited:
                    dfs(curr)
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces+=1
        return provinces