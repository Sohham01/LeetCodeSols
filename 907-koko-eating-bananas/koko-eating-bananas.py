class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hourcheck(k:int) -> bool:
            hours=0
            for i in piles:
                hours+=i//k
                if i%k!=0:
                    hours+=1
                if hours>h:
                    return False
            return True
        l=1
        r=max(piles)
        ans=r
        while l<=r:
            i=(l+r)//2
            if hourcheck(i):
                ans=i
                r=i-1
            else:
                l=i+1
        return ans