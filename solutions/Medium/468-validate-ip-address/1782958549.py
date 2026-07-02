class Solution:
    def validIPAddress(self, IP: str) -> str:


        def isIPV4(IP):
            parts = IP.split('.')
            if len(parts) != 4:
                return False
            for s in parts:
                if len(s) == 0:
                    return False
                try:
                    v = int(s)
                except:
                    return False
                
                if (s[0] == '0' and v != 0):
                    #leading 0
                    return False
                if v == 0 and len(s) > 1:
                    return False
                if v < 0 or v > 255:
                    return False
            return True
        
        def isIPV6(IP):
            parts = IP.split(':')
            if len(parts) != 8:
                return False
            valid = 'abcdefABCDEF0123456789'
            for s in parts:
                if len(s) == 0 or len(s) > 4:
                    return False
                for ch in s:
                    if ch not in valid:
                        return False
            return True
        

        if isIPV4(IP):
            return "IPv4"
        if isIPV6(IP):
            return "IPv6"
        return "Neither"
