class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        s1 = deque(s1.split())
        s2 = deque(s2.split())


        while s1 and s2 and s1[0] == s2[0]:
            s1.popleft()
            s2.popleft()

        while s1 and s2 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()

        return not s1 or not s2