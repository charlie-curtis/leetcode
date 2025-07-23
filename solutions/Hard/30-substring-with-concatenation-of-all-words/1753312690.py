class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        n = len(s)
        m = len(words)
        k = len(words[0])
        C = Counter(words)

        #editorial. Originally I tried the naive n*mk approach where, for each index, you see if the substring concatenation starts at that index. This fails atleast one test case.
        #the new approach capitalizes on the fact that we only need to initiate a sliding window for each index of the string length
        def check(offset):
            
            j = offset
            C2 = Counter()
            out = []
            for i in range(offset, n, k):
                if i + k > n:
                    break
                w = s[i:i+k]
                C2[w]+=1
                while C2[w] > C[w]:
                    w2 = s[j:j+k]
                    C2[w2]-=1
                    j+=k
                if i-j+k == k*m:
                    out.append(j)
            return out

        out = []

        for i in range(k):
            out+=check(i)
        
        out.sort()
        return out
