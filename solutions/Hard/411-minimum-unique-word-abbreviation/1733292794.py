class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:

        INF = 10**9
        n = len(target)
        best = INF
        ans = ""
        sset = set([x for x in dictionary if len(x) == n])

        def bt(cur,input, i, score, readonly):
            nonlocal ans,best

            if i >= n:
                if readonly:
                    seen.add(cur)
                elif score < best and cur not in seen:
                    best = score
                    if not ans:
                        ans = cur
                    else:
                        ans = min(ans, cur)
                else:
                    pass
                    #print(cur)
                return

            #assume we replace everything that is remaining
            bt(cur + str(n-i),input, n, score+1, readonly)
            #assume we don't replace this character
            bt(cur + input[i],input, i+1, score +1, readonly)

            for j in range(i, n-1):
                #see what score is if we replace from [i,j]
                rlength = j-i+1
                bt(cur + str(rlength) + input[j+1],input, j+2, score+2, readonly) #score+2 because we keep the last letter and replace the rest

        seen = set()
        for x in dictionary:
            if len(x) == n:
                bt("",x, 0, 0, True)
        #print(seen)
        bt("",target, 0, 0, False)
        return ans