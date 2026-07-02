class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:



        #had to look at the hints for this one


        m,n = len(mat), len(mat[0])

        l, r = 0, m-1



        while l <= r:
            mid = l + (r-l)//2

            a = -1 if mid-1 < 0 else max(mat[mid-1])
            b = max(mat[mid])
            c = -1 if mid +1 == m else max(mat[mid+1])
            if b > max(a,c):
                break
            if a > c:
                r = mid-1
            else:
                l = mid + 1
            
        
        #print(mid)
        return [mid, mat[mid].index(b)]







        