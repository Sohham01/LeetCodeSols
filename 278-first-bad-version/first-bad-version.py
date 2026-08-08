# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            i=(l+r)//2
            if isBadVersion(i)==False:
                l=i+1
            else:
                r=i-1
        return l