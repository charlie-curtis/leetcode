class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        return sum([1 if x.find(pref) == 0 else 0 for x in words])
        