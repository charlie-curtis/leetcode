class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        ans = 10**9
        def bt(i, groups):
            unused = len([x for x in groups if x == 0])
            if n-i < unused:
                return float('inf')
            if i == n:
                nonlocal ans
                mx = max(groups)
                ans = min(ans, mx)
                return

            
            for j in range(len(groups)):
                groups[j]+=cookies[i]
                bt(i+1, groups)
                groups[j]-=cookies[i]
            
        
        bt(0, [0]*k)
        return ans