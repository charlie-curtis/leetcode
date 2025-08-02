class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = set()
        def bt(i, lists):
            if i == len(nums):
                ans.add(tuple(lists))
                return

            #either don't include this value or do
            bt(i+1, lists)

            lists.append(nums[i])
            bt(i+1, lists)
            lists.pop()


        bt(0, [])


        return [list(x) for x in ans]
        