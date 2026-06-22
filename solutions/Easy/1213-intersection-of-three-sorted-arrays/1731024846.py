class Solution:
    def arraysIntersection(self, A: List[int], B: List[int], C: List[int]) -> List[int]:

        s1, s2, s3 = set(A), set(B), set(C)
        return sorted(list(s1&s2&s3))
        '''
        s2, s3 = set(B), set(C)
        ans = [] 
        for i,x in enumerate(A):
            if x in s2 and x in s3 and A[i-1] != x:
                ans.append(x)
        return ans
        '''
                
        '''
        p1 = p2 = p3 = 0
        m,n,p = len(A), len(B), len(C)

        out = []
        while p1 + p2 + p3 < m + n + p:
            a = 1e15 if p1 == m else A[p1]
            b = 1e15 if p2 == n else B[p2]
            c = 1e15 if p3 == p else C[p3]

            if a == b and b == c:
                if not out or out[-1] != a:
                    out.append(a)
            small = min(a,b,c)
            if a == small:
                p1+=1
            elif b == small:
                p2+=1
            else:
                p3+=1

        return out
        '''

        