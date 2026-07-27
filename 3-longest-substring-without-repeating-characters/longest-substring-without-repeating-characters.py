class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        m=0
        c={}
        for r,i in enumerate(s):
            c[i]=1+c.get(i,0)
            while c[i]>1:
                c[s[l]]-=1
                l+=1
            m=max(m,r-l+1)
        return m