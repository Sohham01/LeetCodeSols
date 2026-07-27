class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b={}
        for i, num in enumerate(nums):
            if target-num in b:
                return [i,b[target-num]]
            b[num]=i