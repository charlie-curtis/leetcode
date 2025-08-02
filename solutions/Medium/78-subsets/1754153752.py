class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        ans = []
        def bt(i, lists):
            if i == len(nums):
                ans.append(lists.copy())
                return

            #either don't include this value or do
            bt(i+1, lists)

            lists.append(nums[i])
            bt(i+1, lists)
            lists.pop()


        bt(0, [])


        return ans
        