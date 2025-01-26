class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], startState: List[int]) -> int:

        n = len(status)
        unlocked = set([i for i in range(n) if status[i]==1])
        reachable = set([x for x in startState])
        q = list(unlocked&reachable)
        processed = set()

        score = 0
        while q:
            idx = q.pop()
            if idx in processed:
                continue
            processed.add(idx)

            score+=candies[idx]
            for nxtkey in keys[idx]:
                if nxtkey in unlocked:
                    continue
                unlocked.add(nxtkey)
                if nxtkey in reachable:
                    q.append(nxtkey)
            for nxtbox in containedBoxes[idx]:
                if nxtbox in reachable:
                    continue
                reachable.add(nxtbox)
                if nxtbox in unlocked or status[nxtbox] == 1:
                    q.append(nxtbox)
        return score





        