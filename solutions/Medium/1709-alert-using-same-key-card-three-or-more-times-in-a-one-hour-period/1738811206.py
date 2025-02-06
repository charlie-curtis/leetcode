class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        d = defaultdict(list)
        for i,x in enumerate(keyName):
            name = x
            time = keyTime[i]

            s1, s2 = time.split(":")
            d[name].append(int(s1)*60+int(s2))



        ans = []
        for name, li in d.items():
            li.sort()
            for i in range(len(li)-2):
                if li[i+2] - li[i] <= 60:
                    ans.append(name)
                    break

        ans.sort()
        return ans
        
        
        