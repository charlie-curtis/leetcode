class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:

        n = len(strs)

        #["lc","evol","cdy"]

        best = None
        for i in range(n): #every word
            for starting_word in [strs[i], strs[i][::-1]]: #both variations of the word, forward and backward
                m = len(starting_word)
                for j in range(m): #every starting letter
                    can = starting_word[j:m]
                    for k in range(n-1): #pair it with every word
                        word = strs[(k+i+1)%n]
                        a,b = word, word[::-1]
                        #append whatever is better btwn the regular word and the reversed word
                        can+=max(a,b)
                    can+=starting_word[:j]
                    if not best or can > best:
                        best = can
        return best


        #azylc | evol | cdy | lc | evol | cdy | azylc
        #clyza

        


