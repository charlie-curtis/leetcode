class Solution:
    def maximumLength(self, A: List[int]) -> int:
        A=[x%2 for x in A]

        ans=max([A.count(x) for x in [0,1]])
        ans=max(ans, len([0 for x in groupby(A)]))
        return ans