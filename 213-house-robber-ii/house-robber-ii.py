class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob_p(nums):
            prev_rob=max_rob=0
            for i in nums:
                temp=max(max_rob,prev_rob+i)
                prev_rob=max_rob
                max_rob=temp
            return max_rob
        return max(rob_p(nums[:-1]),rob_p(nums[1:]))