class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        def center(s,l,r):
            c=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                c+=1
                l-=1
                r+=1
            return c
        for i in range(len(s)):
            res+=center(s,i,i)
            res+=center(s,i,i+1)
        return res