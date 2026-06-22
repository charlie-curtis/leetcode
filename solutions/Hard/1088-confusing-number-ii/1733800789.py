class Solution:
    def confusingNumberII(self, n: int) -> int:

        mmap = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }
        ans = 0
        def bt(cur, rotated, i):
            nonlocal ans
            if cur > n:
                return
            if cur != rotated:
                ans+=1
                
            for x,y in mmap.items():
                if cur == 0 and x == 0:
                    continue
                bt(cur*10+x, y*i+rotated, i*10)

        bt(0, 0, 1)
        return ans
            

