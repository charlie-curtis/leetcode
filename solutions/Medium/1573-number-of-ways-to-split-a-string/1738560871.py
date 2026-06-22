class Solution:
    def numWays(self, s: str) -> int:

        MOD = 10**9 + 7
        cnt = s.count('1')
        n = len(s)
        if cnt == 0:
            @cache
            def dp(i, rem):
                ans = 0
                if rem == 0:
                    print("partition began at", i)
                    ans+=1

                if rem < 0:
                    return 0
                if i == n-1:
                    return ans 


                a = dp(i+1, rem)
                b = dp(i+1, rem-1)

                ans = 0
                ans+=a
                ans%=MOD
                ans+=b
                ans%=MOD
                return ans
                
            return dp(0, 2)


        if cnt % 3 != 0:
            return 0
        out = []
        t = cnt//3
        cur = [] 
        cnt = 0
        for x in s:

            if x == '1' and cnt == t:
                out.append(cur.copy())
                cur = []
                cnt = 0

            cur.append(x)

            if x == '1':
                cnt+=1

        out.append(cur.copy())
        free = []
        cnt = 0
        for x in out[0][::-1]:
            if x == '1':
                break
            cnt+=1
        free.append(cnt+1)

        
        cnt = 0
        for x in out[1][::-1]:
            if x == '1':
                break
            cnt+=1
        free.append(cnt+1)
            

        ans = 1
        for x in free:
            ans*=x
            ans%=MOD
        return ans