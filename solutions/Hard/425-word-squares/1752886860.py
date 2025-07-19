class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        #b a l l
        #a r e a
        #l e a d
        #l a d y

        #this is a hashing problem where we have to consider words of length [1,4]. Count each length independently, and only setup your hashmap
        #for words that are of the length you're checking. In the example above, the length is 4
        #The algorithm is: iterate through all words - choose the first word arbitrarily. It will also be valid since it doesn't have any words to clash with
        #If the first word is ball, then the second word must start with "A". SAy we choose area as the second word.
        #when picking the third word, it must begin with "le". say we picked "lead". When picking the fourth word, it must begin with "lad".
        #Notice that all of these require some sort of prefix, so we can just hash the prefix foreach word and that will allow the backtracking to quickly
        #weed out any non-complaint pairings

        ans = [] 
        def count(cutoff):
            d=defaultdict(list)
            for w in words:
                if len(w) != cutoff:
                    continue
                for i in range(cutoff):
                    h = w[:i+1]
                    d[h].append(w)

            for x in words:
                if len(x) == cutoff:
                    bt([x], cutoff, d)

        def bt(cur, cutoff, d):
            nonlocal ans
            if len(cur) == cutoff:
                ans.append(cur.copy())
                return

            l = len(cur)
            req = ""
            for x in cur:
                req+=x[l]

            for can in d[req]:
                cur.append(can)
                bt(cur, cutoff, d)
                cur.pop()


        for i in range(1,5):
            count(i)
        return ans

