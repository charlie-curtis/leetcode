class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:

        d = defaultdict(set)

        for i in range(len(pid)):
            parent = ppid[i]
            child = pid[i]
            d[parent].add(child)

        
        kill_queue = [kill]

        ans = []
        while kill_queue:
            p = kill_queue.pop()
            ans.append(p)
            for child in d[p]:
                kill_queue.append(child)
        return ans
        