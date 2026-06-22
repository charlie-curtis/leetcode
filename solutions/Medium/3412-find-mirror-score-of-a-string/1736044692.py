class Solution:
    def calculateScore(self, s: str) -> int:

        n = len(s)
        d = defaultdict()

        i = 0
        j = 25

        while i <= j:
            a = chr(i + ord('a'))
            b = chr(j + ord('a'))

            d[a] = b
            d[b] = a
            i+=1
            j-=1


        seen = defaultdict(list)

        ans = 0
        for i in range(n):
            lookingFor = d[s[i]]

            li = seen[lookingFor]
            if len(li) > 0:
                j = li.pop()
                ans+=(i-j)
            else:
                seen[s[i]].append(i)

        return ans
                

        