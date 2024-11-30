class Solution:
    def pathSum(self, nums: List[int]) -> int:


        ans = 0
        sset = set(nums)
        def dfs(num, cur):
            nonlocal ans

            v = num % 10
            pos = num//10 % 10
            d = num//100 % 10


            left = (d+1)*100+(2*pos-1)*10
            found = False
            for i in range(10):
                if left+i in sset:
                    found = True
                    dfs(left+i, cur+v)

            right = (d+1)*100+(2*pos)*10
            for i in range(10):
                if right+i in sset:
                    found = True
                    dfs(right+i, cur+v)

            if not found:
                #print("i am a leaf", num)
                ans+=cur+v


        for i in range(110, 120):
            if i in sset:
                dfs(i, 0)

        return ans

        
        