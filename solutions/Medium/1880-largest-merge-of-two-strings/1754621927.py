class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        A = deque([x for x in word1])
        B = deque([x for x in word2])

        out = []
        while A or B:
            if not A:
                out.append(B.popleft())
            elif not B:
                out.append(A.popleft())
            elif A > B: #note we are comparing the ENTIRE rest of the string here. In case of a tie, we want to uncover the largest 'buried' letter
                out.append(A.popleft())
            else:
                out.append(B.popleft())
        return ''.join(out)
        