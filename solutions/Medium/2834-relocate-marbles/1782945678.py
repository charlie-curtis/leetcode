class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:

        presence = Counter(nums)

        for x,y in zip(moveFrom, moveTo):
            if x == y:
                continue
            presence[y]+=presence[x]
            presence[x] = 0

        return [k for k in sorted(presence.keys()) if presence[k] > 0]