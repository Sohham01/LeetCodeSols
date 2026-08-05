class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        mapping=defaultdict(lambda:-1)
        for i in nums2:
            while st and st[-1]<i:
                mapping[st.pop()]=i
            st.append(i)
        res=[]
        for i in nums1:
            res.append(mapping[i]) 
        return res