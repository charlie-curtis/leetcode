class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:

        if n == 1:
            if k == 0:
                return m
            else:
                return 0


        if m % 2 == 0:
            odd_score = even_score = m//2
        else:
            odd_score = m//2 + 1
            even_score = m//2
        M = 10**9 + 7
        @cache
        def dp(i, prevEven, rem):
            if i == n:
                #we reached the end. As long as it's a valid result, return it
                return 1 if rem == 0 else 0

            if prevEven:
                #if the previous was even, we can either pair it with another even and increment our answer
                a = 0 if rem == 0 else dp(i+1, True, rem-1)*even_score
                a%=M
                #OR we can pair it with an odd
                b = dp(i+1, False, rem)*odd_score
                b%=M
                return (a+b) % M
            else:
                #we can make this number even
                c = dp(i+1, True, rem)*even_score
                c%=M
                d = dp(i+1, False, rem)*odd_score
                d%=M

                #print("returning for i",i,":", c,d, odd_score, even_score)
                return (c+d) % M

        return dp(0, False, k)


        