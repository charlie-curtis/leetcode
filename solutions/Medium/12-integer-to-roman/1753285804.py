class Solution:
    def intToRoman(self, num: int) -> str:


        D = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'], 
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ]


        out = []
        for v, sym in D:
            k = num//v
            if k != 0:
                out+=(k)*sym
                num-=k*v
        
        return ''.join(out)
