class Solution:
    def romanToInt(self, s: str) -> int:

        i = 0
        d = {}
        d['IV'] = 4
        d['IX'] = 9
        d['XL'] = 40
        d['XC'] = 90
        d['CD'] = 400
        d['CM'] = 900
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000

        n = len(s)
        ans = 0
        while i < n:
            if i+1 < n and s[i:i+2] in d:
                ans+=d[s[i:i+2]]
                i+=2
            else:
                ans+=d[s[i]]
                i+=1
        return ans


        