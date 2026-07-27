class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        res=0
        for i in n:
            if i-1 not in n:
                l=1
                while i+l in n:
                    l+=1
                res=max(res,l)
        return res