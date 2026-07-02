class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)
        neigh = [-1]*n
        for i in range(n):
            v = nums[i] % n

            neigh[i] = ((i + v) + n) % n


        def checkDirectionOfPath(path):
            tmp = set()
            for x in path:
                tmp.add(nums[x] < 0)
            return len(tmp) == 1

        print(neigh)    
        overall = set()
        def dfs(i, seen, path):
            if i in seen:
                idx = path.index(i)
                return checkDirectionOfPath(path[idx:])
                    
            
            seen.add(i)
            nxt = neigh[i]
            path.append(i)
            if nxt == i:
                return False
            return dfs(nxt, seen, path)

        
        for i in range(n):
            if i not in overall:
                seen = set()
                if dfs(i,seen, []):
                    return True
                overall.update(seen)
        return False

