class Solution:
    def minLength(self, s: str, numOps: int) -> int:

        lengths = [len(list(g)) for _,g in groupby(s)]
        n = len(s)


        def check1():
            used = 0
            expected = '1'
            for x in s:
                if x != expected:
                    used+=1
                expected = '0' if expected == '1' else '1'
            if used <= numOps:
                return True

            used = 0
            expected = '0'
            for x in s:
                if x != expected:
                    used+=1
                expected = '0' if expected == '1' else '1'
            return used <= numOps
            
                    

        def check(x):
            if x == 1:
                return check1()
            used = 0
            for y in lengths:
                used+=y//(x+1)
            return used <= numOps
                
        n = len(s)
        l = 1
        r = n


        #FFFFFTTTT

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1
        return l