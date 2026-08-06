class Solution:
    def decodeString(self, s: str) -> str:
        cntSt=[]
        strSt=[]
        curr=""
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=="[":
                cntSt.append(num)
                strSt.append(curr)
                curr=""
                num=0
            elif i=="]":
                repeat=cntSt.pop()
                prev=strSt.pop()
                curr=prev+curr*repeat
            else:
                curr+=i
        return curr