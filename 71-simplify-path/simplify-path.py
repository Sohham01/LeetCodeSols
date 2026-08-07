class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split("/")
        st=[]
        for i in a:
            if i=="" or i==".":
                continue
            if i=="..":
                if st:
                    st.pop()
            else:
                st.append(i)
        return "/" + "/".join(st)