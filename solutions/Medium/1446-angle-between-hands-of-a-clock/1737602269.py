class Solution:
    def angleClock(self, h: int, m: int) -> float:

        a = ((h+m/60)*360/12) % 360
        b = (m*360/60) % 360

        print(a,b)

        print(h+m/60)


        c = abs(b-a)

        return min(c, 360-c)
        
        