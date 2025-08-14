class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        sl = SortedList()

        C = Counter()
        out = []
        for x,f in zip(nums, freq):
            if C[x] > 0:
                sl.remove(C[x])
            C[x]+=f
            sl.add(C[x])
            out.append(sl[-1])
        return out

        