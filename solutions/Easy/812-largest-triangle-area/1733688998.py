class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:


        n = len(points)
        def heron(l):
            s = sum(l)/2
            p1 = s - l[0]
            p2 = s - l[1]
            p3 = s - l[2]
            return sqrt(s*p1*p2*p3)
        def get_dist(a,b):
            p1 = (a[0]-b[0])**2
            p2 = (a[1]-b[1])**2
            return sqrt(p1 + p2)
        ans = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue

                    '''
                      A
                     / \
                    B   C
                    '''
                    a = points[i]
                    b = points[j]
                    c = points[k]
                    l1 = get_dist(a,c)
                    l2 = get_dist(c,b)
                    l3 = get_dist(b,a)

                    l = sorted([l1,l2,l3])
                    if l[0] + l[1] > l[2]:
                        ans = max(ans, heron(l))
                    
        return ans
        