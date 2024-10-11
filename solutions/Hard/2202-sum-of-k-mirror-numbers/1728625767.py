class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def check(cur):

            cur = int(cur)
            a = []
            while cur > 0:
                a.append(cur%k)
                cur//=k

            return a == a[::-1]

        odds = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        evens = ['']
        found = ans = 0
        while True:

            tmp = []

            for cur in evens + odds:
                if cur and cur[0] != '0' and check(cur):
                    found+=1
                    ans+=int(cur)
                    if found == n:
                        return ans


            #queue up the even digit numbers first (e.g. '' will become '11', '22', etc.)
            for i in range(10):
                for cur in evens:
                    tmp.append(str(i) + cur + str(i))

            evens = tmp
            tmp = []

            #queue up the odd digit numbers next (e.g. '1' will become '111')
            for i in range(10):
                for cur in odds:
                    tmp.append(str(i) + cur + str(i))

            odds = tmp
            tmp = []