class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        #editorial
        n = len(arr)
        ans=set()
        st=set()
        for x in arr:
            st1=set()
            for y in st:
                st1.add(y|x)
            st1.add(x)
            st=st1
            ans|=st
        return len(ans)