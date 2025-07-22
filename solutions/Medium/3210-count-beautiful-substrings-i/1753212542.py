class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:

        A = []
        n = len(s)
        #for i in range(1,n+1):
        '''
        for i in range(1,int(sqrt(n))+1):
            if i**2 % k//2 == 0:
                A.append(i*2)
        '''

        B = [1 if x in 'aeiou' else 0 for x in s]

        pre = list(accumulate(B, initial=0))
        ans = 0
        for L in range(1,n+1):
            if (L % 2) or (L//2*L//2 %k): continue
            #print("trying lengths", L)
            for i in range(n-L+1):
                cnt = pre[i+L] - pre[i]
                if cnt == L//2:
                    #print("true for", s[i:i+L])
                    ans+=1
        return ans

        return -1


        