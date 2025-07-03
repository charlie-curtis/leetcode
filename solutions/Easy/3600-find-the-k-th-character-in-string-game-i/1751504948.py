class Solution:
    def kthCharacter(self, k: int) -> str:

        cur = [0]
        while len(cur) < k:
            t = len(cur)
            for i in range(t):
                cur.append(cur[i]+1)

        cur = [chr(ord('a') + v%26) for v in cur]
        return cur[k-1]
        