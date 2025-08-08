class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:

        #editorial

        combined = list(zip(aliceValues, bobValues))
        for i,(a,b) in enumerate(combined):
            combined[i] = [a+b, a,b]

        combined.sort(reverse=True)

        alice = bob = 0
        for i in range(len(combined)):
            if i % 2 == 0:
                alice+=combined[i][1]
            else:
                bob+=combined[i][2]
        if bob > alice:
            return -1
        if alice > bob:
            return 1
        return 0
