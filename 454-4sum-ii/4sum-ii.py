class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict=defaultdict(int)
        res=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dict[nums1[i]+nums2[j]]+=1
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                res+=dict[0-(nums3[k]+nums4[l])]
        return res