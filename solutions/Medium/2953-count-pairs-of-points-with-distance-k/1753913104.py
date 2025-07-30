class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:

        n = len(coordinates)
        ans = 0
        C = Counter()
        #x1^x2 + y1^y2 = k
        #a^x2 + b^y2 = k
        for i in range(n):
            x,y = coordinates[i]
            for j in range(k+1):

                #so if we have k = 12
                #we might have 3,9. So we know x1^x2 = 3, y1^y2 = 9
                xval = j
                yval = k-j

                xHash = x^xval
                yHash = y^yval
                ans+=C[(xHash,yHash)]
            C[(x,y)]+=1
        return ans