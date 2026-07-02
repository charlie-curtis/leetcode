class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        #person A has score X, X+1
        #...
        C = Counter()
        h = []
        self.sd = SortedDict()
        for p, t in zip(persons, times):
            C[p]+=1
            heapq.heappush(h, (-C[p], -t, p))
            self.sd[t] = h[0][2]
        #print(self.sd)
        

    def q(self, t: int) -> int:
        idx = self.sd.bisect_right(t)-1
        return self.sd.peekitem(idx)[1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)