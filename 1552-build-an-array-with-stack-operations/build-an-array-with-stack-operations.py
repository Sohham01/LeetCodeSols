class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        a=[]
        for i in range(1,target[-1]+1):
            a.append("Push")
            if i not in target:
                a.append("Pop")
        return a