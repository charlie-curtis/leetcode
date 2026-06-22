class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        M = 10**9 + 7

        fact = [0]*(n+1)
        infact = [0]*(n+1)
        fact[0] = 1
        for i in range(1,n+1):
            fact[i] = i*fact[i-1] % M
            
        infact[-1] = pow(fact[n], M-2, M)
        for i in range(n-1, -1, -1):
            infact[i] = (i+1)*infact[i+1] %M

        pref = [0]*(n+1)
        #from [0,n]
        for i in range(0,n+1):
            #from [0, min(k-1, i)]
            for j in range(min(i+1, k)):
                #iCj
                a = fact[i]
                b = infact[j]
                c = infact[i-j]
                res = a*(b*c%M)%M
                pref[i]+= a*(b*c%M)%M

        ans = 0
        for i in range(n):
            left = i
            right = n-i-1

            a = pref[left]
            b = pref[right]
            t = a + b
            t%=M
            ans+= (t*nums[i])
            ans%=M
        return (ans) %M