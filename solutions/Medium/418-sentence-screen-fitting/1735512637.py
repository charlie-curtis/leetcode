class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        #how many times can we fit a sentence on one line from a given starting pos?


        n = len(sentence)
        totalLength = sum([len(x) for x in sentence])
        @cache

        #given a starting index of i, how many times can we pass N, and what J index does that output us at?
        #so the input will be dp(i), but we need to make sure we have exactly cols remaining
        def dp(i):

            rem = cols
            j = i 
            ans = 0
            while rem - len(sentence[j%n]) >= 0:
                rem-=len(sentence[j%n])
                rem-=1
                j+=1
                if j % n == 0:
                    ans+=1
            return [ans, j%n]

        ans = 0
        i = 0
        for _ in range(rows):
            cnt, i = dp(i)
            ans+=cnt
        return ans