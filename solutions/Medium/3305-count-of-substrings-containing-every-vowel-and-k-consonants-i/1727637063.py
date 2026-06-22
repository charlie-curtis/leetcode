class Solution:
    def countOfSubstrings(self, s: str, k: int) -> int:

        def atleast(k):
            C = Counter()
    
            j = 0
            n = len(s)
    
            def has_all_vowels():
                for x in 'aieou':
                    if C[x] == 0:
                        return False
                return True

            ans = 0
            for i in range(n):
    
                letter = s[i] if s[i] in 'aeiou' else 'con'
                C[letter]+=1
    
                while C['con'] >=k and has_all_vowels():
                    letter = s[j] if s[j] in 'aeiou' else 'con'
                    ans+=len(s)-i
                    C[letter]-=1
                    j+=1
            return ans

        return atleast(k) - atleast(k+1)
