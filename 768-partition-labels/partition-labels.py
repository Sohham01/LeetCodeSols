class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={}
        for i,j in enumerate(s):
            last[j]=i
        res=[]
        start=0
        end=0
        for i,j in enumerate(s):
            end=max(end,last[j])
            if i==end:
                res.append(end-start+1)
                start=i+1
        return res