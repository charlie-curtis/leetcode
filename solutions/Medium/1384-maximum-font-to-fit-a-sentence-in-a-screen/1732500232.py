# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:

        n = len(fonts)
        l = 0
        r = n-1

        def check(idx):
            font = fonts[idx]
            cur_h=fontInfo.getHeight(font)
            if cur_h > h:
                return False
            cur_w = 0
            for x in text:
                cur_w+=fontInfo.getWidth(font, x)
            return cur_w <= w

        while l <= r:
            mid = l+(r-l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1

        #TTTTTTF
        return r if r == -1 else fonts[r]
        