class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]
        for i,x in enumerate(first):
            for j in range(1,len(strs)):
                word = strs[j]
                if i >= len(word) or word[i] != x:
                    return word[:i]

        return first
        