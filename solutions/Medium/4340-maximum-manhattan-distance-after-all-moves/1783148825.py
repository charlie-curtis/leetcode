class Solution:
    def maxDistance(self, moves: str) -> int:

        def fx():
            x = y = 0
            ans = 0
            cnt = 0
            for m in moves:
                if m == '_':
                    cnt+=1
                elif m == 'L':
                    x-=1
                elif m == 'R':
                    x+=1
                elif m == 'U':
                    y+=1
                elif m == 'D':
                    y-=1
                else:
                    raise ValueError("wrong")
            ans = max(ans, abs(y) + abs(x) + cnt)
            return ans

            
        return fx()
                    
        