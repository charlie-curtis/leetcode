class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        d = defaultdict(list)
        for name, time in access_times:
            a = int(time[:2]) * 60
            b = int(time[2:])
            d[name].append(a + b)
        ans = []
        for name, li in d.items():
            li.sort()
            n = len(li)
            for i in range(n-2):
                if li[i+2] - li[i] < 60:
                    ans.append(name)
                    break
        return ans