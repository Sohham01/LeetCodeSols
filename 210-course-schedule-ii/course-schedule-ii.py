class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        for course,p in prerequisites:
            d[course].append(p)
        seen=set()
        path=set()
        op=[]
        def dfs(node):
            if node in path:
                return True
            if node in seen:
                return False
            path.add(node)
            for i in d[node]:
                if dfs(i):
                    return True
            path.remove(node)
            seen.add(node)
            op.append(node)
            return False
        for i in range(numCourses):
            if dfs(i):
                return []
        return op