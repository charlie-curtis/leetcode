class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)

        j = -1
        for i in range(1, len(s)):
            if int(s[i]) < int(s[i-1]):
                j = i
                break
        if j == -1:
            return n
        
        #so j is the out-of-place-idx
        out = ['9']*len(s)
        for i in range(j-1, 0, -1):
            if int(s[i]) - 1 >= int(s[i-1]):
                #found something we can borrow
                out[:i] = s[:i]
                out[i] = str(int(s[i])-1)
                return int(''.join(out))
        
        a = str(int(s[0]) - 1) + '9'*(len(s)-1)
        return int(''.join(a))