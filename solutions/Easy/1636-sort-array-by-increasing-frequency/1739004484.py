class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        C = Counter(nums)
        A = [(v, -k) for (k,v) in C.items()]
        A.sort()


        out = []
        for v, k in A:
            k = -k
            out+= [k]*v
        return out

        