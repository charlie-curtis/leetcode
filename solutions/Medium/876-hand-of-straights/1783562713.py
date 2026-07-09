class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        C = Counter(hand)
        for x in sorted(set(hand)):
            while C[x] > 0:
                for i in range(groupSize):
                    if C[x+i] == 0:
                        return False
                    C[x+i]-=1
        return True
        