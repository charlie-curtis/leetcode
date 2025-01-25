class Solution:
    def numSteps(self, s: str) -> int:

        n = len(s)
        d = deque([x for x in s])
        ans = 0
        while len(d) > 1:
            #print(d)
            if d[-1] == '1':
                ans+=1
                found = False
                for i in range(len(d)-2, -1, -1):
                    if d[i] == '0':
                        #print("found")
                        found = True
                        d[i] = '1'
                        break
                    else:
                        d[i] = '0'
                if not found:
                    #print("wasn't found")
                    d.appendleft('1')

            ans+=1
            d.pop()
        #print(d)
        return ans