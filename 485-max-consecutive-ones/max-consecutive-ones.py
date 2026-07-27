class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=[]
        b=0
        for i in range(len(nums)):
            if nums[i]==1:
                b+=1
            else:
                a.append(b)
                b=0
        a.append(b)
        return max(a)