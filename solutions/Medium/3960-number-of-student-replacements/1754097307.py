class Solution:
    def totalReplacements(self, ranks: List[int]) -> int:

        stack = [ranks[0]]
        ans = 0
        for x in ranks[1:]:
            while stack and stack[-1] > x:
                stack.pop()
            if not stack:
                ans+=1
            stack.append(x)
        return ans