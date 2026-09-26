class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        a=3
        b=2
        curr=0
        for i in range(3,n):
            curr=a+b
            b=a
            a=curr
        return curr