class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:

        seen = set()

        ans = []
        for x in reversed(queries):
            if x in seen:
                continue
            seen.add(x)
            ans.append(x)

        for x in windows:
            if x in seen:
                continue
            seen.add(x)
            ans.append(x)
        return ans
        