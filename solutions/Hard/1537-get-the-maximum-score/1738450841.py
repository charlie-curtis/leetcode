class Solution:
    def maxSum(self, A: List[int], B: List[int]) -> int:

        m,n = len(A), len(B)
        d1 = {}
        d2 = {}
        for i,x in enumerate(A):
            d1[x] = i
        for i,x in enumerate(B):
            d2[x] = i
        MOD = 10**9 + 7
        @cache
        def dp(i, canCross, firstTrack):

            if firstTrack and i == m:
                return 0
            if not firstTrack and i == n:
                return 0

            ans = 0
            a = 0
            if firstTrack:
                #if we are on the first track, we can either cross or stay here
                if canCross:
                    a+=A[i]
                    #stay on track
                    t = dp(i+1, True, True)
                    v = 0
                    if A[i] in d2:
                        nj = d2[A[i]]
                        v = dp(nj, False, False)
                    a+= max(t,v)
                    ans = max(ans,a)
                else:
                    #we can't cross, so we also can't add our value
                    a = dp(i+1, True, True)
                    ans = max(ans,a)
            else:
                #we aren't on the first track
                #we can either cross or stay here
                if canCross:
                    a+=B[i]
                    #stay on track
                    t = dp(i+1, True, False)
                    v = 0
                    if B[i] in d1:
                        nj = d1[B[i]]
                        v = dp(nj, False, True)
                    a+= max(t,v)
                    ans = max(ans,a)
                else:
                    #we can't cross, so we also can't add our value
                    a = dp(i+1, True, False)
                    ans = max(ans,a)
            return ans



        a = dp(0,True, True)
        b = dp(0,True, False)
        return max(a,b) % MOD