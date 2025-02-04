class Solution:
    def maxDistance(self, s: str, k: int) -> int:


        def check(turn):
            used = 0

            x,y = 0,0
            ans = 0
            for c in s:
                if c == 'E':
                    if c in turn and used < k:
                        used+=1
                        x-=1
                    else:
                        x+=1
                elif c == 'W':
                    if c in turn and used < k:
                        used+=1
                        x+=1
                    else:
                        x-=1
                elif c == 'N':
                    if c in turn and used < k:
                        used+=1
                        y-=1
                    else:
                        y+=1
                elif c == 'S':
                    if c in turn and used < k:
                        used+=1
                        y+=1
                    else:
                        y-=1
                ans = max(ans, abs(x) + abs(y))
            return ans


        ans = 0
        for x in ['E', 'W']:
            for y in ['N', 'S']:
                t = set()
                t.add(x)
                t.add(y)
                ans = max(ans, check(t))
                
        return ans
                    
