class Solution:
    def divide(self, top: int, bot: int) -> int:
        low, high = -2**31, 2**31-1
        flag = (bot < 0) ^ (top< 0)
        
        top, bot = abs(top), abs(bot)
        ans = 0
        original = bot

        #repeatedly subtract the divisor from the dividend. To help it converge faster, double the 
        #divisor each time
        while top >= bot:
            i = 1
            while top >= bot:
                ans+=i
                top-=bot
                bot<<=1
                i<<=1
            bot = original

        if flag:
            ans=-ans
        return min(max(ans,low),high)