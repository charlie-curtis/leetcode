class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:


        n = len(deck)
        idxs = deque([i for i in range(n)])

        order = []
        while idxs:
            order.append(idxs.popleft())
            if idxs:
                idxs.append(idxs.popleft())

        vals = deque(sorted(deck))
        out = [0]*n
        for x in order:
            out[x] = vals.popleft()
        return out
        