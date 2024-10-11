class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:


        ans = []

        a = ['6', '9', '0', '8', '1']
        b = ['9', '6', '0', '8', '1']
        d = dict(zip(a,b))

        #n = 8 -> [0, 7], [1,6], [2,5], [3,4]
        #n 1 6
        def bt(cur):

            if len(cur) == n:
                if cur[0] != '0' or n == 1:
                    ans.append(cur)
                return
            if len(cur) > n:
                return

            for k,v in d.items():
                can = k + cur + v
                if not cur and n % 2 == 1:
                    #if n is odd and we're just starting, then we have to start with k == v, so like '0' or '1' or '8'
                    if k == v:
                        bt(k)
                else:
                    bt(can)

        bt("")
        return ans

            