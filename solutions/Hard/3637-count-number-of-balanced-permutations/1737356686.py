class Solution:
    def countBalancedPermutations(self, s: str) -> int:

        A = [int(x) for x in s]
        T = sum(A)
        if T % 2 != 0:
            return 0
        C = Counter(A)

        n = len(s)
        M = 10**9 + 7
        h = max(10, n//2 + 1)
        fact = [0]*(h+1)
        infact = [0]*(h+1)
        fact[0] = 1
        for i in range(1,h+1):
            fact[i] = i*fact[i-1] % M
            
        infact[-1] = pow(fact[h], M-2, M)
        for i in range(h-1, -1, -1):
            infact[i] = (i+1)*infact[i+1] %M



        K = fact[n//2]
        K%=M
        K*=fact[n - n//2]
        K%=M

        @cache
        def dp(i, even, odd, b):
            if i == 10:
                if even+ odd == n and b == 0 and even >= odd and abs(even-odd)<=1:
                    return K
                return 0
            if even > n//2 + 1 or odd > n//2:
                return 0

            ans = 0
            for take in range(0, C[i]+1):
                total = C[i]
                left = take
                right = total-take
                newb = b + left*i - right*i
                a = dp(i+1, even+left, odd+right, newb)

                if a > 0:
                    a*=infact[left]
                    a%=M
                    a*=infact[right]
                    a%=M
                    ans+=a
                    ans%=M
            return ans


        return dp(0, 0, 0, 0)