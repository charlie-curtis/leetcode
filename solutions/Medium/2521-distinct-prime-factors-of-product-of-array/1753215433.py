class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:


        def pfs(x):
            i = 2
            st = set()
            while i*i <= x:
                while x % i == 0:
                    st.add(i)
                    x//=i
                i+=(1 if i == 2 else 2)
            if x > 1:
                st.add(x)
            return st


        st = set()
        for x in nums:
            st|=pfs(x)
        return len(st)
        



        