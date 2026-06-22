class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        C = Counter(nums)
        A = []
        for k in sorted(C.keys(), reverse=True):
            A.append(C[k])
        n = len(A)

        ans = 0
        for i in range(n-1):
            ans+= A[i]
            A[i+1]+=A[i]
        return ans


        