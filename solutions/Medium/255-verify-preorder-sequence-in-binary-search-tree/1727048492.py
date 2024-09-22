class Solution:
    def verifyPreorder(self, pre: List[int]) -> bool:
        
        low, n = 0, len(pre)
        stack = []

        for i in range(n):
            while stack and stack[-1] < pre[i]:
                low = stack.pop()

            if pre[i] < low:
                return False
            stack.append(pre[i])

        return True