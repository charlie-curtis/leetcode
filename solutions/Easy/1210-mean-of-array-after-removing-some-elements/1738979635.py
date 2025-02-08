class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()
        n = len(arr)
        remove = int(n*.05)
        A = arr[remove:-remove]
        return sum(A) / len(A)