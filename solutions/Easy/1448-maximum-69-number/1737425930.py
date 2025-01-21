class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        i = s.find('6')
        if i == -1:
            return num 
        else:
            t = [x for x in s]
            t[i] = '9'
            return int(''.join(t))
        