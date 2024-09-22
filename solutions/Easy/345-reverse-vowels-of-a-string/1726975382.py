class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = [x for x in s if x in 'aeiouAEIOU']

        out = ""
        for x in s:
            out+= vowels.pop() if x in 'aeiouAEIOU' else x
        return out
        