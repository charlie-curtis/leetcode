class Solution:
    def nextClosestTime(self, time: str) -> str:

        arr = []
        for x in time:
            if x.isnumeric():
                arr.append(int(x))
        
        perms = list(product(arr, repeat=4))

        def is_valid(a):

            h = int(a[0]*10 + a[1])
            m = int(a[2]*10 + a[3])
            return 0 <= h <= 23 and 0 <= m <= 59

        def get_dist(a, b):

            original_time = 60*(int(a[0]*10 + a[1])) + int(a[2]*10 + a[3])
            candidate_time = 60*(int(b[0]*10 + b[1])) + int(b[2]*10 + b[3])

            if candidate_time <= original_time:
                candidate_time+=60*24

            return candidate_time - original_time


        
        best = [1e10, ""]
        for x in perms:
            if is_valid(x) and get_dist(arr,x) < best[0]:
                best = [get_dist(arr,x), list(x)]
        z = best[1]
        z = ''.join([str(x) for x in best[1]])
        return z[:2] + ':' + z[2:]
        