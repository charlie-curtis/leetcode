class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:


        n = len(security)
        if time == 0:
            return [x for x in range(n)]

        to_left = [0]*n
        to_right = [0]*n


        for i in range(1,n):
            if security[i] <= security[i-1]:
                to_left[i] = 1 + to_left[i-1]

        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                to_right[i] = 1 + to_right[i+1]

        ans = []
        for i in range(1,n-1):
            if to_left[i] >= time and to_right[i] >= time:
                ans.append(i)

        return ans


        