class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        hours = [1 if x > 8 else -1 for x in hours]

        seen = {0: -1}
        ans = b = 0
        for i,x in enumerate(hours):
            b+=x
            if b-1 in seen:
                ans = max(ans, i-seen[b-1])
            if b not in seen:
                if b-1 in seen:
                    #if we haven't seen this balance before, but we have seen b-1, then use it, because it will still produce a valid answer, and it will be longer
                    seen[b] = seen[b-1]
                else:
                    seen[b] = i
        return ans

        
        # 1, -1, 1
        # 1, 0, 1

        # -1 -2 -3 -4 -5 -4 -3 -2
        # -1 -1 -1 -1 -1 1  1  1
        