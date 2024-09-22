class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        out = ""
        carry = 0
        n = max(len(num1), len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(n):
            a = int(num1[i]) if i < len(num1) else 0
            b = int(num2[i]) if i < len(num2) else 0
            ssum = a + b + carry
            carry = ssum // 10
            out = str(ssum%10) + out
        if carry:
            out = '1' + out
        return out
        