class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        robot.sort()
        factory.sort()

        #dp, where you order all the robots from left to right, and then your dp function is dp(i,j) where i is the next robot that needs
        #to be assigned, and j is the next station. For a given j, we will never revisit it, so we attempt to assign any of the i next i robots up to our capacity
        

        m,n = len(robot), len(factory)
        @cache
        def dp(i,j):
            if i == m:
                #we're done
                return 0
            if j == n:
                #no more available factories, but we didn't fulfill all the robots
                return 1e12

            limit = factory[j][1]
            best = dp(i, j+1) #baseline is if we don't use this
            cur = 0
            for k in range(i,m):
                if k-i+1 > limit:
                    break
                cur+=abs(robot[k] - factory[j][0])
                best = min(cur+dp(k+1,j+1), best)
            return best

        return dp(0,0)