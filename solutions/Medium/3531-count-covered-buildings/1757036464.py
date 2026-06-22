class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:


        mxhor = {}
        mnhor = {}
        mxvert = {}
        mnvert = {}
        for x,y in buildings:
            if x not in mxvert:
                mxvert[x] = y
                mnvert[x] = y
            else:
                mxvert[x] = max(mxvert[x], y)
                mnvert[x] = min(mnvert[x], y)
            if y not in mxhor:
                mxhor[y] = x
                mnhor[y] = x
            else:
                mxhor[y] = max(mxhor[y], x)
                mnhor[y] = min(mnhor[y], x)
        

        ans = 0
        for x,y in buildings:
            if (mxvert[x] > y > mnvert[x]) and (mxhor[y] > x > mnhor[y]):
                ans+=1
        return ans
        