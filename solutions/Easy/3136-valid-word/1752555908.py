class Solution:
    def isValid(self, word: str) -> bool:

        word = word.lower()
        vowels = 'aeiou'
        cons = 'bcdfghjklmnpqrstvwxyz'

        a = len(word) >= 3
        b = any([x in vowels for x in word])
        c = any([x in cons for x in word])
        d = all([x.isdigit() or x.isalpha() for x in word])

        return all([a,b,c,d])