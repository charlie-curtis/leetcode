class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        ones = []
        twos = []
        ssum = 0
        for x in nums:
            ssum+=x
            if x % 3 == 1:
                ones.append(x)
                if len(ones) > 2:
                    #at most, we only need 2 values
                    ones.sort()
                    ones = ones[:2]
            if x % 3 == 2:
                twos.append(x)
                if len(twos) > 2:
                    #at most, we only need 2 values
                    twos.sort()
                    twos = twos[:2]

        INF = 10**9
        if ssum % 3 == 0:
            return ssum
        if ssum % 3 == 1:
            #we either need to remove the smallest one or two twos
            a = b = INF
            if len(ones) >= 1:
                a = ones[0]
            if len(twos) >= 2:
                b = sum(twos[:2])
        elif ssum % 3 == 2:
            #we either need to remove the smallest two or two ones
            a = b = INF
            if len(twos) >= 1:
                a = twos[0]
            if len(ones) >= 2:
                b = sum(ones[:2])

        return ssum - min(a,b)