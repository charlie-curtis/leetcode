from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, mat: List[List[int]], k: int) -> int:

        m, n = len(mat), len(mat[0])
        pref = []
        pref.append([0]*(n+1))
        for i in range(m):
            pref.append(list(accumulate(mat[i], initial=0)))


        def check(width):
            #print("checking a width of", width)
            best = -1e15
            for j in range(width-1, n): #j is the initial position, and j-width is the end position
                #print("checking width", width, "and starting pos", j)
                l = ssum = 0
                sl = SortedList()
                sl.add(0)
                for i in range(m):
                    ssum+=pref[i+1][j+1] - pref[i+1][j+1-width]

                    idx = sl.bisect_left(ssum-k)
                    if idx!= len(sl):
                        best = max(best, ssum - sl[idx])
                    sl.add(ssum)

            #print("best for that width was", best)
            return best


        best = -1e15 
        #we are going to do a sliding window over all the widths
        for i in range(1,n+1): #i is the width
            best = max(best,check(i)) #i goes from 1 to n

        return best
        