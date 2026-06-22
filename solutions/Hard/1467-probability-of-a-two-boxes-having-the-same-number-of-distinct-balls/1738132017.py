class Solution:
    def getProbability(self, balls: List[int]) -> float:

        n = len(balls)
        t = sum(balls)
        @cache
        def dp(i, c1, c2, used):
            #print("IN", i, c1,c2)
            if i == n:
                res = int(c1 == c2 and used*2 == t)
                if res:
                    return [1,0]
                elif used*2 == t:
                    return [0,1]
                else:
                    return [0,0]

            ans = [0,0] 
            V = balls[i]
            for k in range(0,V+1):
                C = comb(V,k)
                a = c1 + (1 if k !=0 else 0)
                b = c2 + (1 if k != V else 0)
                c = dp(i+1, a,b, used+k)
                #print(C,c, "lOOK")
                ans[0]+= C*c[0]
                ans[1]+= C*c[1]
                #we can place 1 ball in x, v-1 balls in y
                #nCr
                #but then since these are unique, we need to multiply by something
            return ans

        b = dp(0, 0, 0, 0)
        return b[0] / sum(b)