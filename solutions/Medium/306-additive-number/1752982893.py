class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)

        def isleadingzero(cur):
            if int(cur) == 0:
                return False
            return not str(int(cur)) == cur

        def bt(i, cur, prev1, prev2):

            if i == n:
                if prev2 == -1:
                    return False
                if prev1 + prev2 != int(cur):
                    return False
                if isleadingzero(cur):
                    return False
                return True
            
            #append to current
            if bt(i+1, cur+num[i], prev1, prev2):
                return True

            if cur and not isleadingzero(cur) and (prev2 == -1 or (prev2!=-1 and prev1+prev2 == int(cur))):
                return bt(i+1, num[i], int(cur), prev1)
            return False


        return bt(0, '', -1, -1)


            
        