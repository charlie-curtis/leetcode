class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        #the "exactly one replacement" scenario made me think that something like [HIGH, HIGH, HIGH] would have to be downgraded to [HIGH, HIGH, HIGH-1] to satisfy the replacement -- apparently we can "replace" an element with its same value
        HIGH = 10**5
        LOW = -10**5

        pos = sorted([x for x in nums if x > 0])
        neg = sorted([x for x in nums if x < 0])[::-1]
        
        options = []
        #case 1. Use 3 positives to make an answer
        if len(pos) >= 2:
            options.append(pos[-2]*pos[-1]*HIGH)

        #case 2. Use 2 negatives and 1 positive (use 1 pos 1 neg, add neg)
        if len(neg) >= 1 and len(pos) >= 1:
            options.append(pos[-1]*neg[-1]*LOW)
        #case 3. use 2 negatives and 1 positive (use 2 neg, add pos)
        if len(neg) >= 2:
            options.append(neg[-1]*neg[-2]*HIGH)
        #case 4. return 0
        options.append(0)


        return max(options)