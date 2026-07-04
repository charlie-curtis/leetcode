class Solution:
    def punishmentNumber(self, n: int) -> int:


        @cache
        def check(x, target):
            if x == target:
                return True
            if target <= 0:
                return False

            s = str(x)
            m = len(s)
            if len(s) == 1:
                return False
            #print(s)
            for i in range(m-1):
                y = int(s[0:i+1])
                r = int(s[i+1:])
                if check(r, target-y):
                    return True
            return False

        


        return sum([i*i if check(i*i, i) else 0 for i in range(1,n+1)])