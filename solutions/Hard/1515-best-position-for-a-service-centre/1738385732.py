class Solution:
    def getMinDistSum(self, B: List[List[int]]) -> float:

        #this problem is hard. I originally tried to do a divide-and-conquer where I split the grid into 4 rectangles
        #and used the best answer, but that turned out to have small precision issues which lead me to believe at
        #some point i took a wrong turn and the algorithm couldn't self heal because the boundaries always get smaller -- never bigger


        #this problem is unintuitive -- especially with teh "found" usage
        dirs = [[-1,0], [1,0], [0,1], [0,-1]]

        def fn(x,y):
            return sum([sqrt((a-x)**2 + (b-y)**2) for (a,b) in B])

        E = .00000000000000000001
        step = 100
        x,y = 0,0
        best = 1e15
        while step > E:
            found = False
            for dx,dy in dirs:
                canx, cany = x + dx*step, y + dy*step
                can = fn(canx,cany)
                if can < best:
                    best = can
                    x,y = canx,cany
                    #apparently if we found a better answer, we don't want to cut the step which I guess can make sense
                    found = True
                    break
            if not found:
                step/=2
        return best