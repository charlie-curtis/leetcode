class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        if num == 0:
            return 0 


        for i in range(10):
            if num < 0:
                return -1
            unit = num % 10
            if unit == k:
                return i + 1
            num-=k

        return -1

        