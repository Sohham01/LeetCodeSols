class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            x=0
            for j in nums:
                if j<i:
                    x+=1
            ans.append(x)
        return ans