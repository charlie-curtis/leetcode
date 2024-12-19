class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:

        mmap = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]


        n = len(word)
        ans = 0
        for k in range(1,n+1):
            j = 0
            ssum = 0
            for i in range(n):
                t = ord(word[i]) - ord('a')
                ssum+=mmap[t]

                if i-j+1 > k:
                    t = ord(word[j]) - ord('a')
                    ssum-=mmap[t]
                    j+=1
                
                if i - j + 1 == k and (ssum % (i-j+1)) == 0:
                    ans+=1
        return ans


        