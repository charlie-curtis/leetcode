class Solution:
    def minimumSteps(self, s: str) -> int:

        #0's come first
        zeros = s.count('0')
        #0's will be in the range [0, zeros-1]
        #so if there are 2 zeros, they need to go in i = 0 or i = 1
        j = 0
        ans = 0
        for i,x in enumerate(s):
            if s[i] == '0' and i >= zeros: #if a '0' is found in the backhalf of the array, simulate a swap
                #find a suitable j index that needs to be swapped
                while j < zeros and s[j] == '0':
                    j+=1
                #simulate swapping the j and i
                ans+=i-j
                j+=1
        return ans


        