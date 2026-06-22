class Solution:
    def countSubranges(self, A: List[int], B: List[int]) -> int:

        n = len(A)

        M = 10**9+7

        @cache
        def dp(i, balance):
            print(i, balance)
            if i == n:
                return 0

            
            #optionA - extend subarray by adding to A
            sums = [balance+A[i], balance-B[i]]
            ans=len([x for x in sums if x == 0])
            ans%=M
            ans+=dp(i+1, balance+A[i])
            ans%=M
            #optionB - extend subarray by adding to B
            ans+=dp(i+1, balance-B[i])
            ans%=M
            return ans

        ans = 0
        for i in range(n):
            ans+=dp(i, 0)
            ans%=M
        return ans
        