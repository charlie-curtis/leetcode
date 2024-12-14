class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:

        n = len(sensor1)

        #if this is bad, we will be able to skip the first mismatch and match everything else
        def isgood(s,t):
            i = 0
            j = 0
            while i < n and j < n:
                if s[i] != t[j]:
                    if i-j != 0:
                        return False
                    i+=1
                    if i == n:
                        return False
                    if s[i] != t[j]:
                        return False
                i+=1
                j+=1
            return i - j == 1
        
        a = isgood(sensor1, sensor2)
        b = isgood(sensor2, sensor1)

        if a and not b:
            return 2
        if b and not a:
            return 1
        return -1




        