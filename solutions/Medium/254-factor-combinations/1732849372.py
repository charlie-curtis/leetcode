class Solution:
    def getFactors(self, n: int) -> List[List[int]]:


        def f(x):
            out = []
            i = 2
            while i*i <= x:
                while x % i == 0:
                    out.append(i)
                    x//=i
                i+=1 if i == 2 else 2

            if x > 1:
                out.append(x)

            return out


        seen = set()
        def backtrack(cur):

            t = tuple(sorted(cur))
            if t in seen:
                return
            seen.add(t)

            for i in range(len(cur)):
                for j in range(i+1,len(cur)):
                    a = cur[:i]
                    b = cur[i+1:j]
                    c = cur[j+1:]
                    d = [cur[i]*cur[j]]
                    backtrack(a+b+c+d)


        backtrack(f(n))
        return [list(x) for x in seen if len(x) > 1]