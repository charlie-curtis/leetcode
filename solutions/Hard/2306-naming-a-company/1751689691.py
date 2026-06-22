class Solution:
    def distinctNames(self, ideas: List[str]) -> int:


        n = len(ideas)
        H = defaultdict(set)
        for x in ideas:
            H[ord(x[0]) - ord('a')].add(x[1:])
        

        ans = 0
        for i in range(26):
            if i not in H:
                continue
            s1 = H[i]
            for j in range(i+1,26):
                if j not in H:
                    continue
                s2 = H[j]
                k = len(s1.intersection(s2))
                ans+=2*(len(s1)-k) * (len(s2)-k)
        return ans
                
