class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        l_total=0
        for i in range(len(nums)):
            r_total=total-l_total-nums[i]
            if r_total==l_total:
                return i
            l_total+=nums[i]
        return -1