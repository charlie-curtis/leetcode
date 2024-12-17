class Solution:
    def toHexspeak(self, num: str) -> str:

        ans = 0
        num = int(num)
        out = []
        while num > 0:
            out.append(num%16)
            num//=16


        mapping = ['A', 'B', 'C', 'D', 'E', 'F']
        ans = ""
        for x in out[::-1]:
            if x == 0:
                ans+='O'
            elif x == 1:
                ans+='I'
            elif 10 <= x <= 15:
                ans+=mapping[x-10]
            else:
                return "ERROR"
        return ans