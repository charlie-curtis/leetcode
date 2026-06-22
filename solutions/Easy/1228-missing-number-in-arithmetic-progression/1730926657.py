class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        n = len(arr)
        jump = (arr[-1] - arr[0]) // n
        expected = arr[0]
        for x in arr:
            if x != expected:
                return expected
            expected+=jump

        return arr[0]
        