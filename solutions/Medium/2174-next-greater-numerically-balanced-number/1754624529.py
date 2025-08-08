class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def good(i):
            C = Counter([int(x) for x in str(i)])
            for i in range(10):
                if C[i] == 0:
                    continue
                if C[i] != i:
                    return False
            return True


        for i in count(n+1):
            if good(i):
                return i