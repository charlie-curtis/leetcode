class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        n = len(s)
        j = 0
        vowels = 0
        ans = 0
        for i,x in enumerate(s):
            if x in 'aeiou':
                vowels+=1

            if i-j+1 > k:
                if s[j] in 'aeiou':
                    vowels-=1
                j+=1

            if i-j + 1 == k:
                ans = max(ans, vowels)

        return ans
        