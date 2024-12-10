class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:

        if str1 == str2:
            return True

        mapp = {}
        for a,b in zip(str1,str2):
            if a in mapp and mapp[a] != b:
                return False
            mapp[a] = b
        l = len(set([x for x in str2]))

        #this last part through me for a loop. I originally tried to do unique checking on str1
        #then I did a lot of weird complicated cycle stuff. Ultimately, the answer involved looking at str2
        #this is because if str2 has less than 26 unique characters, then one of the following must be true

        #1. str1 has less than 26 unique characters, and we can therefore use a "swap" character
        #2. str1 has 26 unique characters, and therefore atleast 2 characters in str1 must map to the same
        #character in str2 (pigeonhole principle), thus granting us our swap character

        return l != 26
