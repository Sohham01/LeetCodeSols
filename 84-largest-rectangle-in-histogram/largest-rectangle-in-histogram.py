class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[-1]
        area=0
        for i in range(len(heights)):
            while st[-1]!=-1 and heights[i]<=heights[st[-1]]:
                height=heights[st.pop()]
                width=i-st[-1]-1
                area=max(area,height*width)
            st.append(i)
        while st[-1]!=-1:
            height=heights[st.pop()]
            width=len(heights)-st[-1]-1
            area=max(area,height*width)
        return area