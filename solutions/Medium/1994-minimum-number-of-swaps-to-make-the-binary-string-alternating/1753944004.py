class Solution:
    def minSwaps(self, s: str) -> int:

        n=len(s)
        ones=s.count('1')
        zeros=s.count('0')

        def diff(cur):
            ans=0
            for x in s:
                if int(x) != cur:
                    ans+=1
                cur^=1
            return ans//2
        if n % 2 == 0 and ones == zeros:
            return min(diff(0),diff(1))
        if n%2 == 1 and max(zeros,ones) - min(zeros, ones) == 1:
            return diff(1) if ones > zeros else diff(0)
        return -1
                