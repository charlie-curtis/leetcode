class Solution:
    def findKthBit(self, n: int, k: int) -> str:


        cur = [0]
        while len(cur) < k:
            tmp = cur + [1] + [x^1 for x in cur][::-1]
            cur = tmp
        return str(cur[k-1])
        