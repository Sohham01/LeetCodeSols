class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        res=0
        i=0
        for j in range(len(s)):
            freq[s[j]]+=1
            maxFreq=max(freq.values())
            curLen=j-i+1
            if curLen-maxFreq>k:
                freq[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res