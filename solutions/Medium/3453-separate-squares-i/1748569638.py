class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:


        l = 0
        r = 10**9 + (5*10**4)

        #FFFFFFFFTTTTTTT

        #true if horizontal line has greater area below 
        def check(mid):
            above = 0
            below = 0
            for x,y, li in squares:
                if y >= mid:
                    #all above
                    above+=(li*li)
                elif y + li <= mid:
                    #all below
                    below+=(li*li)
                else:
                    #below is y to mid
                    below+=(mid-y)*li

                    #above is mid to y+li
                    above+=(y+li - mid)*li
                    #intersection
                #print("cur is ", above, below)
            #print("ABOVE, BELOW", above, below)
            return above <= below
        i = 0
        #TTTTFFFF
        while r-l >= .00001:
            mid = l + (r-l)/2
            #print("mid is ", mid, l,r)
            if check(mid):
                r = mid
            else:
                l = mid

        return r
        