class Solution:
    def distance(self, nums: List[int]) -> List[int]:


        # 3, 2, 3, 9, 2,2
        # [0, 2]
        # [1, 4,5,7,10,17,19,23,...]
        # [3]

        #A = [2,7,2,4,0]

        d = defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)

        n = len(nums)
        out = [0]*n
        for l in d.values():

            m = len(l)
            for i in range(m):
                if i == 0:
                    cur = sum([x - l[0] for x in l])
                else:
                    delta = l[i] - l[i-1]
                    before = i-1
                    after = m-1-i
                    cur+=before*delta
                    cur-=after*delta
                out[l[i]] = cur
        return out