class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        #editorial for DP solution
        #the idea is that we count the prefix of 0s. When we encounter a 1, it'll take either t+1 seconds OR # of zero seconds
        #(whichever is greater)

        #in other words, the timing will either be bottlenecked
        #because there are a bunch of 1s in the string OR it will be bottlenecked by flipping 0s

        t = 0
        zeros = 0
        j = s.find('0')
        if j == -1: return 0 #trim any leading 1s because they are free
        s = s[j:]
        for i,x in enumerate(s):
            if x == '0':
                zeros+=1
            else:
                t = max(t+1, zeros)
        return t

