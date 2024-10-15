class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:


        #TTTTTFFFFFF
        #return r
        #>=k

        n = len(s)
        l = 1 
        r = n-1

        def check(i):

            C = Counter()
            for j in range(n-i+1):
                t = s[j:j+i]
                C[t]+=1
                if C[t] > 1:
                    return True
            return False


        while l <= r:

            mid = l + (r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
        