class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while a and temperatures[i]>temperatures[a[-1]]:
                d=a.pop()
                res[d]=i-d
            a.append(i)
        return res