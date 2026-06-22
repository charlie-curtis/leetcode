class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:


        if k > 1:
            return ''.join(sorted(s))

        ans = s
        cur = s
        for i in range(len(s)):
            cur = cur[1:] + cur[0]
            ans = min(ans, cur)
        return ans


            
