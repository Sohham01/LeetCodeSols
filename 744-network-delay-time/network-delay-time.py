class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist=[float('inf')]*(n+1)
        dist[k]=0
        heap=[(0,k)]
        while heap:
            d,node=heapq.heappop(heap)
            if d>dist[node]:
                continue
            for neighbour, weight in graph[node]:
                if d+weight<dist[neighbour]:
                    dist[neighbour]=d+weight
                    heapq.heappush(heap,(dist[neighbour],neighbour))
        res=0
        for i in range(1,n+1):
            if dist[i]==float('inf'):
                return -1
            res=max(res,dist[i])
        return res