class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        a = set(source)
        b = set(target)

        if len(a&b) < len(b):
            return -1
        m = len(source)
        n = len(target)


        ans = 0
        i = 0
        while ans < len(target):
            ans+=1
            for j in range(m):
                if source[j] == target[i]:
                    i+=1
                if i == n:
                    return ans

        raise ValueError("Wrong")