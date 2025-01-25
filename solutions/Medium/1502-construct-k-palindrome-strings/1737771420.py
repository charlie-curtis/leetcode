class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            print("h1")
            return False

        C = Counter(s)
        odds = 0
        for v in C.values():
            if v % 2 == 1:
                odds+=1
        if odds > k:
            return False
        return True
        