class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        C = Counter(s)
        odds = 0
        for k,v in C.items():
            if v % 2 == 1:
                odds+=1
        return odds <= 1
        