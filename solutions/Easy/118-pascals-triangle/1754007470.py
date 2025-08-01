class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = [[1]]
        for i in range(1,numRows):
            cur = []
            for j in range(i+1):
                s = 0
                if j-1 >= 0:
                    s+=ans[i-1][j-1]
                if j < len(ans[i-1]):
                    s+=ans[i-1][j]
                cur.append(s)
            ans.append(cur)
        return ans
        