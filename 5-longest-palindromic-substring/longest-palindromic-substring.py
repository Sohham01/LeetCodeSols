class Solution:
    def longestPalindrome(self, s: str) -> str:
        def center(s:str, l:int, r:int):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        a=0
        b=0
        for i in range(len(s)):
            odd=center(s,i,i)
            even=center(s,i,i+1)
            max_len=max(odd,even)
            if max_len>b-a:
                a=i-(max_len-1)//2
                b=i+(max_len)//2
        return s[a:b+1]