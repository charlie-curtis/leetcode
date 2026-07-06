class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        losses = Counter()
        for w, l in matches:
            losses[l]+=1
            losses[w]+=0

        oneloss = []
        noloss = []
        for k in sorted(losses.keys()):
            v = losses[k]
            if v == 0:
                noloss.append(k)
            if v == 1:
                oneloss.append(k)
        
        return [noloss, oneloss]


        