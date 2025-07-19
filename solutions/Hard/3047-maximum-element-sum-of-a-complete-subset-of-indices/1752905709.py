class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def categorize(x):

            i = 2
            out = []
            while i*i <= x:
                cnt = 0
                while x % i == 0:
                    cnt+=1
                    x//=i
                if cnt % 2 == 1:
                    out.append(i)
                i+=1 if i % 2 == 0 else 2
            if x > 1:
                out.append(x)
            
            return 1 if not out else reduce(lambda x,y: x*y, out)
        

        C = Counter()
        for i,x in enumerate(nums):
            #print(categorize(i+1))
            C[categorize(i+1)]+=x

        return max(C.values())


        