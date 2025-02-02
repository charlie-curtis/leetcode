class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        MOD = 10**9 + 7

        #this problem was difficult and i relied on the editorial


        def dfs(A):
            n = len(A)
            if n <= 1:
                return 1
            left = [x for x in A if x < A[0]]
            right = [x for x in A if x > A[0]]

            print(n-1)
            P = comb(n-1, len(left))

            return (dfs(left)*dfs(right)*P) % MOD

        return dfs(nums) - 1