class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:

        INF = 10**9
        def do(i,j):
            nonlocal s

            if i >= j:
                return 0

            k = j
            while s[i] != s[k] and i < k:
                k-=1
            if i == k:
                #if this is an odd length string,
                #and we encounter the middle element
                #just reverse from the other side to avoid handling this case
                s = s[::-1]
                return do(i,j)
            
            s[k:j+1] = s[k+1:j+1] + [s[k]]
            return do(i+1,j-1) + j-k

        s = [x for x in s]
        C = Counter(s)
        n = len(s)
        return do(0, n-1)