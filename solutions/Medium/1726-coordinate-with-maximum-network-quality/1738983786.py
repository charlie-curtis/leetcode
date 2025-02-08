class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:

        #problem is terrible
        points = towers
        def get(x,y):
            score = 0
            for a,b, q in points:
                d = (x-a)*(x-a) + (y-b)*(y-b)
                if d <= radius*radius:
                    c = int((q / (1+sqrt(d))))
                    score+= c
            return score

        best = 0
        ans = [0,0]
        for x in range(51):
            for y in range(51):
                score = get(x,y)
                if score > best or (score == best and tuple(ans) > (x,y)):
                    ans = [x,y]
                    best = score
        return ans