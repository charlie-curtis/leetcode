class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        st = set()
        def format(x):
            return ''.join(sorted([y for y in str(x)]))
        for i in range(32):
            st.add(format(1<<i))
        return format(n) in st