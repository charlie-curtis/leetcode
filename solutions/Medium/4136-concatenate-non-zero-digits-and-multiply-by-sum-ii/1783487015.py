class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        #MODULAR INVERSE REQUIRED
        n = len(s)
        digitsum = [0] * (n+1)
        consum = [0] * (n+1)
        scaled = [0] * (n+1)

        cnt = 0
        MOD = 10**9 + 7
        last_multiplier = 1
        for i in range(n-1, -1, -1):
            x = int(s[i])
            digitsum[i] = digitsum[i+1] + x

            if x != 0:
                consum[i] = consum[i+1] + x*last_multiplier
                consum[i]%=MOD
                cnt+=1
                last_multiplier*=10
                last_multiplier%=MOD
            else:
                consum[i] = consum[i+1]
            scaled[i] = cnt

        out = []
        for l,r in queries:
            ssum = digitsum[l] - digitsum[r+1]
            inv10 = pow(10, -1*scaled[r+1], MOD)
            x = ((consum[l] - consum[r+1]) * inv10) % MOD

            #print(ssum,x)

            out.append(ssum*x % MOD)
        return out

        