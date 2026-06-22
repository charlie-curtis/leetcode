class Solution:
    def closestToTarget(self, A: List[int], target: int) -> int:

        #find the closet value above target
        #find the closet value below target
        nums = A

        ans = 1e15
        n = len(A)
        j = 0
        C = Counter()
        def add(x):
            C['_cnt_']+=1
            for i in range(20):
                if x&(1<<i) > 0:
                    C[i]+=1
        def sub(x):
            C['_cnt_']-=1
            for i in range(20):
                if x&(1<<i) > 0:
                    C[i]-=1
        def get():
            out = 0
            for i in range(20):
                if C[i] == C['_cnt_']:
                    out|=(1<<i)
            return out

        #try to keep this below target
        for i,x in enumerate(nums):

            add(x)
            while j < i:
                sub(nums[j])
                if get() > target:
                    add(nums[j])
                    break
                j+=1
            #print(get())
                
            ans = min(ans, abs(get() - target))

        j = 0
        C = Counter()
        #try to keep this above target
        for i,x in enumerate(nums):

            add(x)
            while j < i and get() < target:
                #if it sinks below target, then increase it by removing some nums from the left
                sub(nums[j])
                j+=1
            ans = min(ans, abs(get() - target))
        return ans
        