class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        a=[0]*n
        b=[]
        prev=0
        for i in range(len(logs)):
            iden,stat,ts=logs[i].split(":")
            iden=int(iden)
            ts=int(ts)            
            if stat=="start":
                if b:
                    top=b[-1]
                    a[top]+=ts-prev
                b.append(iden)
                prev=ts
            else:
                top=b.pop()
                a[top]+=ts-prev+1
                prev=ts+1
        return a