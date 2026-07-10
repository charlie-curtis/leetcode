class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []

        i = 2
        out = []
        while finalSum >= i:
            out.append(i)
            finalSum-=i
            i+=2
        
        out[-1]+=finalSum
        return out