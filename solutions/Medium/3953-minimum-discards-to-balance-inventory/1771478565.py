class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:

        H = defaultdict(list)

        ans = 0
        for i,x in enumerate(arrivals):
            #if we haven't even seen m occurrences of this item in general
            #or we have seen atleast m-occurences, but there aren't more than m in our window
            if len(H[x]) < m or (i-H[x][-m]) >= w:
                H[x].append(i)
            else:
                ans+=1
        return ans




        
        